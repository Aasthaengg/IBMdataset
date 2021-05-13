# coding: utf-8
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

D=[]

for i in range(N):
    D.append(A[i]-B[i])

D.sort()

k=0
need=0
ans=0
while D[k]<0 and k!=N:
    need+=D[k]
    k+=1
    ans+=1

l=-1
while need<0 and D[l]>0:
    need+=D[l]
    ans+=1
    l-=1

if need<0:
    print(-1)
else:
    print(ans)