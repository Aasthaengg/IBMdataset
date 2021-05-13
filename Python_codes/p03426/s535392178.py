from itertools import accumulate
import sys

input=sys.stdin.readline

H,W,D=map(int,input().split())
A=[[] for i in range(0,H)]
for i in range(0,H):
    A[i]=list(map(int,input().split()))
Q=int(input())
L=[0 for i in range(0,Q)]
R=[0 for i in range(0,Q)]
for i in range(0,Q):
    L[i],R[i]=map(int,input().split())

data=[(0,0) for i in range(0,H*W+1)]
for i in range(0,H):
    for j in range(0,W):
        data[A[i][j]]=(i+1,j+1)
anstable=[[] for i in range(0,D+1)]
for i in range(1,D+1):
    x=(H*W-i)//D
    for j in range(0,x):
        s=data[i+j*D][0]
        t=data[i+j*D][1]
        s2=data[i+(j+1)*D][0]
        t2=data[i+(j+1)*D][1]
        anstable[i].append(abs(s2-s)+abs(t2-t))
    anstable[i]=list(accumulate(anstable[i]))

for i in range(0,Q):
    x=L[i]%D
    if x==0:
        x=D
    if D>=L[i]:
        if R[i]==L[i]:
            print(0)
        else:
            if x!=D:
                print(anstable[x][R[i]//D-1])
            else:
                print(anstable[x][R[i]//D-2])
    else:
        if x!=D:
            print(anstable[x][R[i]//D-1]-anstable[x][L[i]//D-1])
        else:
            print(anstable[x][R[i]//D-2]-anstable[x][L[i]//D-2])
