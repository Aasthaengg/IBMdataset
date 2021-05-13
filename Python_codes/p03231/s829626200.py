n,m=map(int,input().split())
s=input()
t=input()

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

L=lcm(n,m)

isGood=True
cycle_s=L//n
cycle_t=L//m
cycle_lcm=lcm(cycle_s,cycle_t)
for i in range((L//cycle_lcm)):
    if s[cycle_lcm*i//cycle_s]!=t[cycle_lcm*i//cycle_t]:
        isGood=False
        break

if(isGood):
    print(L)
else:
    print(-1)