import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
path = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)
parent = [-1]*n
size = [1]*n
d = [0]*n
def dfs(now):
    for nxt in path[now]:
        if nxt != parent[now]:
            parent[nxt] = now
            d[nxt] = d[now] + 1
            size[now] += dfs(nxt)
    return size[now]
dfs(0)
cnt = 0
now = n-1
for i in range((d[n-1]+1)//2 - 1):
    now = parent[now]
if size[now] >= n - size[now]:
    print('Snuke')
else:
    print('Fennec')
