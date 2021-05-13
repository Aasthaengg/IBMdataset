import sys

N,H=map(int,input().split())
A=[0]*N
B=[0]*N

for i in range(N):
    a,b=map(int,input().split())
    A[i],B[i]=a,b

max_A=max(A)
B.sort(reverse=True)

K=0
for b in B:
    if H>0 and b>=max_A:
        K+=1
        H-=b

if H>0:
    K+=(H+max_A-1)//max_A

print(K)