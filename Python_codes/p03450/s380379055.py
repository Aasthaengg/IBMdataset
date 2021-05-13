# coding: utf-8
# Your code here!
import sys

sys.setrecursionlimit(10**9)

def dfs(l,d):
    loc[l]=d
    for n_l,n_d in way[l]:
        if loc[n_l]==10**9:
            dfs(n_l,d+n_d)
        elif loc[n_l]!=d+n_d:
            print("No")
            exit()

N,M=map(int,input().split())

way=[[] for i in range(N)]
loc=[10**9]*N

for _ in range(M):
    L,R,D=map(int,input().split())
    way[L-1].append([R-1,D])
    way[R-1].append([L-1,-D])

for i in range(N):
    if loc[i]==10**9:
        dfs(i,0)

print("Yes")