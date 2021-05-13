import fractions
N,M=map(int,input().split())
S=input()
T=input()

n=N//fractions.gcd(N,M)
m=M//fractions.gcd(N,M)
g=fractions.gcd(N,M)
judge=True

for i in range(g):
    if S[i*n]!=T[i*m]:
        judge=False

if judge==True:
    print(N*M//g)
else:
    print(-1)