import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = sys.stdin.readline

node_num, path_num = map(int, input().split())
graph = [[] for _ in range(node_num)]

for i in range(path_num):
    from_node, to_node = map(int, input().split())
    graph[from_node - 1].append(to_node - 1)
#print(graph)

#dp[i]はiを始点としたときの経路長の最大値
dp = [-1] * node_num

def rec(v):
    #print(v)
    #print(dp)
    if dp[v] > -1:
        return dp[v]
    else:
        dp[v] = 0
        for nv in graph[v]:
            dp[v] = max(dp[v], rec(nv) + 1)
        return dp[v]

ans = 0
for node in range(node_num):
    ans = max(ans, rec(node))
print(ans)