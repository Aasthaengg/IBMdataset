
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
AB = [list(map(int,input().split())) for _ in range (N-1)]
edge = [[] for _ in range(N)]
for u,v in AB:
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

dists = [0]*N
distn = [0]*N
def dfs_s(v, p):
    for nv in edge[v]:
        if nv==p:continue 
        dists[nv] = dists[v] + 1
        dfs_s(nv, v)
    return 
def dfs_n(v, p):
    for nv in edge[v]:
        if nv==p:continue 
        distn[nv] = distn[v] + 1
        dfs_n(nv, v)
    return 
dfs_s(0,-1)
dfs_n(N-1,-1)

B = 0
W = 0
for i in range(N):
    if dists[i]<=distn[i]:
        B += 1
    else:
        W += 1

if B>W:
    print('Fennec')
else:
    print('Snuke')


