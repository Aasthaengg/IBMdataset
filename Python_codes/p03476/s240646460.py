#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
q=int(input())
def primes(n):
    m=int(pow(n,0.5))
    is_prime=[True]*(n+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,m+1):
        if not is_prime[i]:
            continue
        for j in range(i*2,n+1,i):
            is_prime[j]=False
    return [i for i in range(n+1) if is_prime[i]]
s=set(primes(10**5))
count=[0]*(10**5+1)
count[1]=0
count[2]=0
for i in range(3,10**5+1):
    if i in s and (i+1)//2 in s:
        count[i]=count[i-1]+1
    else:
        count[i]=count[i-1]
for i in range(q):
    l,r = map(int,input().split())
    print(count[r]-count[l-1])
