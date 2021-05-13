
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N,M = map(int,input().split())

xy = [list(map(int,input().split())) for _ in range (M)]

# DAG TopoSort
in_count = [0]*N
edge = [[] for _ in range(N)]
for u,v in xy:
    in_count[v-1] += 1
    edge[u-1].append(v-1)

S = []
L = [] #Sort結果
index = [0]*N # 頂点vのLにおけるインデックスindex[v]
for i in range(N):
    if in_count[i]==0: S.append(i)
while S:
    v = S.pop()
    index[v] = len(L)
    L.append(v)
    for nv in edge[v]:
        in_count[nv] -= 1
        if in_count[nv]==0:
            S.append(nv)

dp = [0] * N
for i,v in enumerate(L):
    for nv in edge[v]:
        dp[index[nv]] = max(dp[index[nv]], dp[i]+1)

print(max(dp))
