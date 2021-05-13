import sys
sys.setrecursionlimit(1000000000)

n,m = map(int,input().split())
G = [[] for _ in range(n)]
INF = float("INF")
pos = [INF]*n
for _ in range(m):
    l,r,d = map(int,input().split())
    l -= 1
    r -= 1
    G[l].append((r,d))
    G[r].append((l,-d))

def dfs(now):
    for nxt,d in G[now]:
        if pos[nxt] == INF:
            pos[nxt] = pos[now]+d
            dfs(nxt)
        elif pos[nxt] != pos[now]+d:
            print("No")
            exit()

for i in range(n):
    if pos[i] == INF:
        pos[i] = 0
        dfs(i)
print("Yes")