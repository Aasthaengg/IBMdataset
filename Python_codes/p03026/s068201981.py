import sys
sys.setrecursionlimit(20000)

def add_node_2_tree_dic(tree_dic, x, y):
    if x not in tree_dic:
        tree_dic[x] = [y]
    else:
        tree_dic[x].append(y)

#   深さ優先探索で行けそう

N = int(input())
tree_dic = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    add_node_2_tree_dic(tree_dic, a, b)
    add_node_2_tree_dic(tree_dic, b, a)

c_lst = list(map(int, input().split()))
c_lst.sort()
ans_lst = [0]*N

def search_next_node_and_add_side_wate(tree_dic, ans, current_node, c_lst, ans_lst):
    next_node_lst = tree_dic[current_node][:]

    for next_node in next_node_lst:
        c = c_lst.pop()
        ans += c
        ans_lst[next_node - 1] = c

        tree_dic[current_node].remove(next_node)    #   今回通った枝を取り払う
        tree_dic[next_node].remove(current_node)

        if len(tree_dic[current_node]) == 0:
            del tree_dic[current_node]#   探索し終えたノードの削除
        if len(tree_dic[next_node]) == 0:
            del tree_dic[next_node]#   探索し終えたノードの削除
        else:   #   次のノードにつながっている辺があるとき
            ans = search_next_node_and_add_side_wate(tree_dic, ans, next_node, c_lst, ans_lst)

    return ans


ans = 0
current_node = 1
ans_lst[0] = c_lst.pop()
ans = search_next_node_and_add_side_wate(tree_dic, ans, current_node, c_lst, ans_lst)


ans_str = ""
for i in range(N):
    ans_str += str(ans_lst[i])
    if i != N - 1:
        ans_str += " "


print(ans)
print(ans_str)
