import sys
sys.setrecursionlimit(10000000)

V, M = map(int,input().split())
L = [[] for _ in range(V+1)]
DP = [-1 for _ in range (V + 2)]
for _ in range(M):
    x,y = map(int,input().split())
    L[x-1].append(y-1)

def rec(v):
    if DP[v] != -1: return DP[v]
    ret = 0
    for x in L[v]:
        ret = max(ret,rec(x)+1)
    DP[v] = ret
    return DP[v]
ans = 0
for i in range(V):
    ans = max(ans, rec(i))
print(ans)
