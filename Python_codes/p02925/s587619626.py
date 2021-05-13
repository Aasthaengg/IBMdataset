ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
sys.setrecursionlimit(10**6)

n = ni()
def idx(u,v):
    return u*n+v
tree = [[] for i in range(n**2)]
go=[False]*n**2
back=[False]*n**2
memo = [1]*n**2 #memo[i] iからの深さ
start = []
for i in range(n):
    A1 = lma()
    pu,pv = i,A1[0]-1
    if pu>pv:pu,pv=pv,pu
    start.append(idx(pu,pv))
    for j in range(1,n-1):
        u,v = i,A1[j]-1
        if u>v:u,v=v,u
        tree[idx(pu,pv)].append(idx(u,v))
        pu,pv=u,v
        start.append(idx(pu,pv))
#print(tree)
def dfs(s):
    go[s]=True
    for node in tree[s]:
        if not go[node]:
            memo[s] = max(dfs(node)+1,memo[s])
        else:
            if back[node]:
                memo[s] = max(memo[node]+1,memo[s])
            else:
                print(-1)
                exit()
    back[s]=True
    return memo[s]
ans = 0
for s in start:
    if not go[s]:
        ans = max(ans,dfs(s))
print(ans)
