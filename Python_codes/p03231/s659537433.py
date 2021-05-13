from fractions import gcd
lcm=lambda x,y:x//gcd(x,y)*y
N,M=map(int, input().split())
S=input()
T=input()
g=gcd(N,M)
if all(S[N//g*i]==T[M//g*i] for i in range(g)):
    print(lcm(N,M))
else:
    print(-1)