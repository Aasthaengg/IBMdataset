# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
from fractions import gcd
from functools import lru_cache

#############
# Constants #
#############

MOD = 10**9 +7
INF = float('inf')

#############
# Functions #
#############

######INPUT######
def inputI(): return int(input().strip())
def inputS(): return input().strip()
def inputIL(): return list(map(int,input().split()))
def inputSL(): return list(map(str,input().split()))
def inputILs(n): return list(int(input()) for _ in range(n))
def inputSLs(n): return list(input().strip() for _ in range(n))
def inputILL(n): return [list(map(int, input().split())) for _ in range(n)]
def inputSLL(n): return [list(map(str, input().split())) for _ in range(n)]

#####Inverse#####
def inv(n): return pow(n, MOD-2, MOD)

######Combination######
kaijo_memo = []
def kaijo(n):
  if(len(kaijo_memo) > n):
    return kaijo_memo[n]
  if(len(kaijo_memo) == 0):
    kaijo_memo.append(1)
  while(len(kaijo_memo) <= n):
    kaijo_memo.append(kaijo_memo[-1] * len(kaijo_memo) % MOD)
  return kaijo_memo[n]

gyaku_kaijo_memo = []
def gyaku_kaijo(n):
  if(len(gyaku_kaijo_memo) > n):
    return gyaku_kaijo_memo[n]
  if(len(gyaku_kaijo_memo) == 0):
    gyaku_kaijo_memo.append(1)
  while(len(gyaku_kaijo_memo) <= n):
    gyaku_kaijo_memo.append(gyaku_kaijo_memo[-1] * pow(len(gyaku_kaijo_memo),MOD-2,MOD) % MOD)
  return gyaku_kaijo_memo[n]

def nCr(n,r):
  if(n == r):
    return 1
  if(n < r or r < 0):
    return 0
  ret = 1
  ret = ret * kaijo(n) % MOD
  ret = ret * gyaku_kaijo(r) % MOD
  ret = ret * gyaku_kaijo(n-r) % MOD
  return ret

######Factorization######
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])
    return arr

#####LCM#####
def lcm(a, b):
    return a * b // gcd (a, b)

#############
# Main Code #
#############

N,M = inputIL()
A = inputIL()

MAX = max(A)

imos = [0]*(MAX*2+2)
imos[0] = N

for i in A:
  imos[i+1] -= 1
for i in range(1,len(imos)):
  imos[i] = imos[i-1]+imos[i]


def count_m(X):
  m = 0
  for i in A:
    m += imos[max(0,X-i)]
  return m

upper = MAX*2
lower = 0
X = (upper+lower)//2
m = count_m(X)


#print(m,X,lower,upper)
while upper != lower:
  if m > M:
    temp = lower
    lower = (upper+lower-1)//2
    if lower == temp:
      lower += 1
  else:
    temp = upper
    upper = (upper+lower+1)//2
    if upper == temp:
      upper -= 1
  X = (upper+lower+1)//2
  m = count_m(X)
  #print(m,X,lower,upper)

  
imos2 = [0]*(MAX*2+2)
for i in A:
  imos2[0] += i
  imos2[i+1] -= i
for i in range(1,len(imos2)):
  imos2[i] = imos2[i-1]+imos2[i]
  
ans = 0
for i in A:
  ans += i*imos[max(X-i,0)]+imos2[max(X-i,0)]
  
print(ans-(m-M)*X)
