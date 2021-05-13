#028_A
from fractions import gcd

N,M=map(int,input().split())
S=input()
T=input()
flg=True

g=gcd(N,M)
n,m=N//g,M//g

for k in range(0,g):
    if S[k*n]!=T[k*m]:
        flg=False

print(N*M//g if flg else -1)