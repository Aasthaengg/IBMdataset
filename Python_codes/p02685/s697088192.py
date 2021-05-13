#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
#mod = 10**9 + 7
mod=998244353
x=220000
fact=[0 for i in range(x)]
invfact=[0 for i in range(x)]
fact[0]=1

def cmod(n,k,mod):
    if n<0 or n<k:
        return 0
    return (fact[n]*invfact[n-k]*invfact[k])%mod
for i in range(1,x):
    fact[i]=(fact[i-1]*i)%mod
#print(fact)
invfact[-1]=pow(fact[-1],mod-2,mod)
#print(invfact)
for j in range(x-1,0,-1):
    #print(j)
    invfact[j-1]=(invfact[j]*(j))%mod
#print(invfact)

n,m,k=MI()
beki=[0 for i in range(n)]
beki[0]=m%mod
for i in range(n-1):
    beki[i+1]=(beki[i]*(m-1))%mod
    
ans=0

for i in range(k+1):
    j=n-i-1
    ans+=(beki[j]*cmod(n-1,i,mod))%mod
    #print(beki[j]*cmod(n-1,i,mod))
print(ans%mod)