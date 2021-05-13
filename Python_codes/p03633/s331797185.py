#最大公約数
def gcd(m,n):
    from math import gcd as g
    return g(m,n)
        
def GCD(*X):
    from functools import reduce
    return reduce(gcd,X)

#最小公倍数
def lcm(m,n):
    return (m//gcd(m,n))*n

def LCM(*X):
    from functools import reduce
    return reduce(lcm,X)


N=int(input())
T=[]
for i in range(N):
    T.append(int(input()))
print(LCM(*T))
