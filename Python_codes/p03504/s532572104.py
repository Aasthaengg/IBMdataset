# coding: utf-8
# Your code here!
N,C=map(int,input().split())

log=[[0]*C for i in range(10**5)]


for _ in range(N):
    s,t,c=map(int,input().split())
    log[s-1][c-1]+=1
    log[t-1][c-1]-=1

ans=0
temp=0
for i in range(10**5):
    plus=log[i].count(1)
    temp+=plus
    ans=max(ans,temp)
    minus=log[i].count(-1)
    temp-=minus
#print(log[:15])
print(ans)

