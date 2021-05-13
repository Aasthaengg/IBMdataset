a,b = map(int,input().split())
mod = 10**9+7
x = (2*a-b)//3
y = (2*b-a)//3

if (2*a-b)%3 != 0 or (2*b-a)%3 != 0 or 2*b < a or 2*a < b or (a+b)%3 != 0:
    print(0)
    exit()

def comb(n,r):
    fact = 1
    invfact = 1
    for i in range(r):
        fact *= n-i
        fact %= mod
        invfact *= i+1
        invfact %=mod
    return fact*pow(invfact,mod-2,mod)%mod

print(comb(x+y,y))