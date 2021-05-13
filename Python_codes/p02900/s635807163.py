from math import gcd

def factorization(N):
    res=[]
    for i in range(2,int(N**(1/2))+2):
        if not N%i:
            r=0
            while not N%i:
                N//=i
                r+=1
            res.append((i,r))
    if N>1:
        res.append((N,1))
    return res
a,b=map(int,input().split())
g=gcd(a,b)
print(1+len(factorization(g)))