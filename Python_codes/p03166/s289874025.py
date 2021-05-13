import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    edge[a-1].append(b-1)
dpv = [-1]*N

def dp(v):
    if dpv[v] != -1:
        return dpv[v]
    if len(edge[v])==0:
        dpv[v]=0
        return 0
    res = 0
    for w in edge[v]:
        res = max(dp(w),res)
    res += 1
    dpv[v] = res
    return res

def solve():
    for i in range(N):
        dp(i)
    ans = max(dpv)
    # print(dpv)
    return ans
print(solve())