ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys

def is_primes(n):
    n+=1
    primes = [1]*n
    primes[0] =0
    primes[1] =0
    for i in range(2,int(n**0.5)+1):
        if primes[i] ==1:
            for j in range(2*i,n,i):
                primes[j] = 0
    return primes
def iscomb(n):
    for p in primes:
        if p>n**0.5+1:
            return False
        if n%p==0:
            return True


n = ni()
nm=55555
isprimes = is_primes(nm)
primes = [p for p in range(nm) if isprimes[p]]
i=0
ans=[]
while len(ans)<n:
    if primes[i]%5==1:
        ans.append(primes[i])
    i+=1
print(*ans)
