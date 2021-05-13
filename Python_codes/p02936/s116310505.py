import sys
sys.setrecursionlimit(10**6)
 
n, q = map(int, input().split())
connect = [set() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    connect[a-1].add(b-1)
    connect[b-1].add(a-1)
 
counter = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    counter[p-1] += x
 
ans = [0] * n
 
def dfs(count, v, parent):
    count += counter[v]
    ans[v] = count
    for child in connect[v]:
        if child != parent:
            dfs(count, child, v)
 
dfs(0, 0, -1)
 
print(*ans)