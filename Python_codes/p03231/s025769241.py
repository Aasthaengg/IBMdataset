from fractions import gcd
N,M=map(int,input().split())
S=input()
T=input()
g=gcd(N,M)
n=N//g
m=M//g
s=[]
t=[]
for i in range(N):
    if i%n==0:
        s.append(S[i])
for j in range(M):
    if j%m==0:
        t.append(T[j])
for x,y in zip(s,t):
    if x!=y:
        print(-1)
        exit()
print(M*N//g)