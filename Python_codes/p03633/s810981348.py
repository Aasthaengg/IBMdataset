N=int(input())
T=[int(input()) for i in range(N)]

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

ans=T[0]
for i in range(1,N):
    ans=lcm(ans,T[i])
print(ans)