from fractions import gcd
N,M=map(int,input().split())
S=input()
T=input()
l=gcd(N,M)
print(N*M//l if all(S[i*N//l]==T[i*M//l] for i in range(l)) else "-1")
