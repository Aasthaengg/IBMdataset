# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
import bisect
from collections import deque
from fractions import gcd
from functools import lru_cache


#############
# Constants #
#############

MOD = 10**9+7
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

#####BitCount#####
def bit_count(n):
  count = 0
  while n:
    n &= n -1
    count += 1
  return count

#############
# Main Code #
#############

N = inputI()
A = inputILL(N)

class WarshallFloyd():
  def __init__(self, N):
    self.N = N
    self.d = [[float("inf") for i in range(N)] for i in range(N)]

  def add(self, u, v, c, directed=False):
    if directed is False:
      self.d[u][v] = c
      self.d[v][u] = c
    else:
      self.d[u][v] = c

  def WarshallFloyd_search(self):
    for k in range(self.N):
      for i in range(self.N):
        for j in range(self.N):
          self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
    hasNegativeCycle = False
    for i in range(self.N):
      if self.d[i][i] < 0:
        hasNegativeCycle = True
        break
    for i in range(self.N):
      self.d[i][i] = 0
    return hasNegativeCycle, self.d
  
graph = WarshallFloyd(N)
for i in range(N):
  for j in range(N):
    graph.add(i,j,A[i][j])
    
hasNegativeCycle, d = graph.WarshallFloyd_search()

for i in range(N):
  for j in range(N):
    if A[i][j] > d[i][j]:
      print(-1)
      exit()

ans = 0
for i in range(N):
  for j in range(i+1,N):
    flag = 1
    for k in range(N):
      if k!=i and k!=j:
        if d[i][k]+d[k][j] <= A[i][j]:
          flag = 0
    if flag:
      ans += A[i][j]
print(ans)