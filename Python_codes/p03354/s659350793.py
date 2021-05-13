# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**9)

def dfs(loc,num):
    root[loc]=num
    for item in plan[loc]:
        if root[item]==-1:
            dfs(item,num)
    return 0

N,M=map(int,input().split())

P=list(map(int,input().split()))

plan=[[]for i in range(N)]
root=[-1]*N

for _ in range(M):
    a,b=map(int,input().split())
    plan[a-1].append(b-1)
    plan[b-1].append(a-1)

for i in range(N):
    if root[i]==-1:
        dfs(i,i)

ans=0
for i in range(N):
    if root[i]==root[P[i]-1]:
        ans+=1
#print(root)
print(ans)