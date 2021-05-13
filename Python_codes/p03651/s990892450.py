import sys
from fractions import gcd

input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

g=A[0]
for i in range(0,N):
    g=gcd(g,A[i])

m=max(A)
if K%g==0 and m>=K:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')