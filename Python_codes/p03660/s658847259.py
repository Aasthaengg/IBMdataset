import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
pre = [None]*n
def dfs(node, p_node=-1):
    for c_node in graph[node]:
        if c_node==p_node:
            continue
        pre[c_node] = node
        dfs(c_node, node)
dfs(0)
path = [n-1]
now = n-1
while now>0:
    now = pre[now]
    path.append(now)
snuke = path[len(path)//2-1]
fennec = path[len(path)//2]
def dfs2(node, p_node):
    cnt = 1
    for c_node in graph[node]:
        if c_node==p_node:
            continue
        cnt += dfs2(c_node, node)
    return cnt
print('FSennunkeec'[dfs2(fennec, snuke)<=dfs2(snuke, fennec)::2])