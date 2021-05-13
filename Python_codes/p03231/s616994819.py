from fractions import gcd
def lcm(a,b):
    return(a*b//gcd(a,b))

N,M=map(int,input().split())
S,T=input(),input()

_lcm=lcm(N,M)
n=_lcm//N
m=_lcm//M
for i in range(0,_lcm,n*m):
    if S[i//n]!=T[i//m]:
        print(-1)
        exit()    
print(_lcm)
