import fractions
N,M=map(int,input().split())
S=input()
T=input()
g=fractions.gcd(N,M);l=N*M//g
if(g==1):
    print(l if S[0]==T[0] else -1)
    exit()
n=N//g;m=M//g
for i in range(g):
    if(S[n*i]!=T[m*i]):
        print(-1)
        exit()
print(l)