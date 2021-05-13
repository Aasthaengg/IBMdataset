import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)

def dp(v,dpv,e):
    if dpv[v] != -1:
        return dpv[v]
    if len(e[v])==0:
        dpv[v]=0
        return 0
    res = 0
    for w in e[v]:
        res = max(dp(w,dpv,e),res)
    res += 1
    dpv[v] = res
    return res

def solve(edge):
    dpv = [-1]*N
    for i in range(N):
        dp(i,dpv,edge)
    ans = max(dpv)
    # print(dpv)
    return ans
print(solve(edge))