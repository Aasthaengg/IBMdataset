# -*- coding: utf-8 -*-

#############
# Libraries #
#############

import sys
input = sys.stdin.readline

import math
from collections import deque
from fractions import gcd
from functools import lru_cache


#############
# Constants #
#############

MOD = 998244353
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

N = inputI()
S = inputSLs(N)


is_start = 0
is_end = 0
is_both = 0

data_s = []
data_m = []

for item in S:
  if item[0] == "(" and item[-1] == ")":
    is_both += 1
  elif item[0] == "(":
    is_start += 1
  elif item[-1] == ")":
    is_end += 1
  s = 0
  m = 0
  for i in item:
    if i == "(":
      s += 1
    else:
      s -= 1
      m = min(s,m)
  data_s.append(s)
  data_m.append(m)

    
def final():
  A = []
  B = []
  C = []
  D = []
  for i in range(N):
    s = data_s[i]
    m = data_m[i]
    if m == 0 and s>=0:
      A.append(s)
    elif m < 0 and s>=0:
      B.append([m,s])
    elif m<0 and m<s<0:
      C.append([s-m,s])
    else:
      D.append(s)

  B.sort(reverse=True)
  C.sort()
  #print(A,B,C,D)
  left = sum(A)
  right = -sum(D)
  #print(left,right)
  for item in B:
    left += item[0]
    if left<0:
      return "No"
    left -= item[0]
    left += item[1]
  for item in C:
    right -= item[0]
    if right<0:
      return "No"
    right += item[0]
    right -= item[1]
  return "Yes"
      

if sum(data_s) == 0:
  if is_start>0 and is_end >0:
    print(final())
    exit()
  elif is_start == 0 and is_end >0:
    if is_both >= 1:
      print(final())
      exit()
  elif is_start > 0 and is_end ==0:
    if is_both >= 1:
      print(final())
      exit()
  else:
    if is_both >= 2:
      print(final())
      exit()    
print("No")

 
