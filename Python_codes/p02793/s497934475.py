def get_sieve_of_eratosthenes_new(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

def ord(N,n):#N,nは正の整数、Nで割り切れる回数、許容はN^1000
    if n%N!=0:
        return 0
    else:
        return 1+ord(N,n//N)

prime=get_sieve_of_eratosthenes_new(1000)

N=int(input())
A=list(map(int,input().split()))
mod=10**9+7

data=[[0 for i in range(0,len(prime))] for i in range(0,N)]
nokori=[1 for i in range(0,N)]
largeprime=set([])

import copy
sample=copy.copy(A)
for i in range(0,N):
    for j in range(0,len(prime)):
        a=ord(prime[j],A[i])
        data[i][j]=a
        A[i]=A[i]//(prime[j]**a)

    if A[i]!=1:
        largeprime.add(A[i])
    nokori[i]=A[i]

lcm=[max(data[i][j] for i in range(0,N)) for j in range(0,len(prime))]
largeprime=list(largeprime)

LCM=1
for i in range(0,len(lcm)):
    LCM=(LCM*pow(prime[i],lcm[i],mod))%mod

for i in range(0,len(largeprime)):
    LCM=(LCM*largeprime[i])%mod

ans=0
for i in range(0,N):
    ans=(ans+LCM*pow(sample[i],mod-2,mod))%mod

print(ans)