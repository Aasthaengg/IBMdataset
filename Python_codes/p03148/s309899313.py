import sys
import heapq as h

input=sys.stdin.readline

N,K=map(int,input().split())
sushi=[[0,0] for i in range(0,N)]
for i in range(0,N):
    t,k=map(int,input().split())
    sushi[i][1]=t
    sushi[i][0]=k

sushikind=[[] for i in range(0,N+1)]
for i in range(0,N):
    sushikind[sushi[i][1]].append(sushi[i][0])

kindmax=[0 for i in range(0,N+1)]

for i in range(0,N):
    if sushikind[i]:
        kindmax[i]=max(sushikind[i])

sushi.sort(reverse=True)
sum=0
kind=[]
kind=set(kind)
extra=[]
flag=[0 for i in range(0,N+1)]
for i in range(0,K):
    sum+=sushi[i][0]
    kind.add(sushi[i][1])
    if sushi[i][0]==kindmax[sushi[i][1]]:
        if flag[sushi[i][1]]==1:
            extra.append(sushi[i][0])
        else:
            flag[sushi[i][1]]=1
    else:
        extra.append(sushi[i][0])


set={i for i in range(1,N+1)}
set-=kind
appendix=[kindmax[i] for i in set if kindmax[i]!=0 ]
extra.sort()
appendix.sort(reverse=True)
k=len(kind)
first=k
ans=k**2+sum
for i in range(k,min(K,k+len(appendix))):
    k+=1
    sum+=appendix[k-first-1]-extra[k-first-1]
    test=k**2+sum
    if test>ans:
        ans=test

print(ans)