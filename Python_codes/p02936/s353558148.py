import sys
sys.setrecursionlimit(10**7)

n, q = map(int, input().split())
ans = [0 for _ in range(n)]
trees = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    trees[a-1].append(b-1)
    trees[b-1].append(a-1)

for _ in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x

visited = [False]*n
def dfs(n):
    visited[n] = True
    for i in trees[n]:
        if visited[i]:
            continue
        ans[i] += ans[n]
        dfs(i)
dfs(0)
for i in ans:
    print(i)

