# coding: utf-8
# Your code here!
N=int(input())

A=[]
B=[]
C=[]
for _ in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(a+b)

s_A=sum(A)
s_B=sum(B)
C.sort(reverse=True)

ans=s_A
for i in range(N)[1::2]:
    ans-=C[i]

print(ans)

