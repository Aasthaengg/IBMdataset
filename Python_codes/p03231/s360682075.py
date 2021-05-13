from math import gcd

N,M=map(int,input().split())
S=input()
T=input()

G=gcd(N,M)
L=(N*M)//G

P=L//N
Q=L//M

A=range(0,L,P)
B=range(0,L,Q)

F=True
for k in A:
    if k in B:
        F&=S[k//P]==T[k//Q]
if F:
    print(L)
else:
    print(-1)