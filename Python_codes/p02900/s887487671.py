#n=int(input())
a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

def prime_factorize(n):
    n_origin=n+0
    primelist=[]
    a=2
    while a*a<=n_origin:
        if n%a!=0:
            a+=1
            continue
        ex=0
        while n%a==0:
            ex+=1
            n=n//a
        primelist.append([a,ex])
        a+=1
    if n!=1:
        primelist.append([n,1])
    return primelist

import math
gcd=math.gcd(a,b)#最大公約数
primelist=prime_factorize(gcd)
print(len(primelist)+1)
