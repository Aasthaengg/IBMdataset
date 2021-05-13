from fractions import gcd
N,M=map(int,input().split(' '))
S=input()
T=input()
G=gcd(N,M)
L = N*M//G
ln = list(range(0,L,(N//G)))
lm = list(range(0,L,(M//G)))
for i,j in zip(ln,lm):
    if i>=N or j>=M:
        break
    if S[i] != T[j]:
        print(-1)
        exit()
print(L)