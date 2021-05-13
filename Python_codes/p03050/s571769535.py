#素因数分解
def Prime_Factorization(n):
    R=[]
    N=n

    for k in range(2,int(-(-n**0.5//1))+1):
        if N%k==0:
            C=0
            while N%k==0:
                C+=1
                N//=k
            R.append([k,C])

    if N!=1:
        R.append([N,1])
        
    if not R:
        R.append([N,1])

    return R

#約数全部
from copy import copy
def Divisors(n):
    if n==1:
        return [1]
    
    L=Prime_Factorization(n)
    U=[1]

    for (p,k) in L:
        T=copy(U)
        for t in T:
            r=t
            for _ in range(1,k+1):
                r*=p
                U.append(r)
    U.sort()
    return U


import sys
N=int(input())
if N==1:
    print(0)
    sys.exit()
    
L=Divisors(N)
L.remove(1)

K=0
for a in L:
    b=a-1
    if N//b==N%b:
        K+=b
print(K)
