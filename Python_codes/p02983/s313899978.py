import sys

L,R=map(int,input().split())
M=2019

R=min(R,L+2*M-1)

X=M+1
for i in range(L,R+1):
    for j in range(i+1,R+1):
        X=min(X,(i*j)%M)
print(X)
