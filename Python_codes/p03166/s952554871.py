import sys

sys.setrecursionlimit(500000)


N,M = list(map(int,input().split()))

e_list = [[] for i in range(N)]

for i in range(M):
    x,y = list(map(int,input().split()))
    x,y = x-1,y-1
    e_list[x].append(y)

memo = [-1]*N

def DFS(v):
    if memo[v]!=-1:
        return memo[v]
    if len(e_list[v])==0:
        memo[v] = 0
        return 0
    res = 0
    for v1 in e_list[v]:
        res1 = DFS(v1)
        if res<res1+1:
            res = res1+1
    memo[v] = res
    return res

ans = 0
for i in range(N):
    res = DFS(i)
    if res>ans:
        ans = res
print(ans)