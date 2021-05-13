import sys
sys.setrecursionlimit(10**7)

n = int(input())
graph = {i : [] for i in range(n)}
for i in range(n-1):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

stack = [0]
already = set()
parent = [i for i in range(n)]
flg = False
while len(stack) > 0:
    cur = stack.pop(-1)
    already.add(cur)
    for _next in graph[cur]:
        if _next not in already:
            stack.append(_next)
            parent[_next] = cur
            if _next == n - 1:
                flg = True
                break
    if flg:
        break

path = []
cur = n - 1
while cur != 0:
    path.append(cur)
    cur = parent[cur]
path.append(0)
path.reverse()
flg_2 = len(path) % 2 != 0
left = path[len(path) // 2 - 1 + flg_2]
right = path[len(path) // 2 + flg_2]

def dfs(x, last):
    res = 1
    for _next in graph[x]:
        if _next != last:
           res += dfs(_next, x)
    return res

left_res = dfs(left, right)
#print(left_res)
print("Fennec" if left_res > (n - left_res) else "Snuke")
