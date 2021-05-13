import fractions
N,M=map(int,input().split())
S=input()
T=input()
g=fractions.gcd(N,M);l=N*M//g
if(g==1):
    print(l if S[0]==T[0] else -1)
    exit()
a,b=0,0
n=N//g;m=M//g
while(a<N and b<M):
    if(S[a]!=T[b]):
        print(-1)
        exit()
    a+=n;b+=m
print(l)
