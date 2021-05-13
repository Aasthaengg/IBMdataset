# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 08:44:21 2020

@author: teppe
"""

from collections import deque

def prepare(n, MOD):
 
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, MOD - 2, MOD)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
     
    return factorials, invs

MOD = 10**9+7
fact, fact_inv = prepare(10+10**5, MOD)

def perm(n,k):
  if k > n or k < 0:
    return 0
  return fact[n] * fact_inv[n-k] % MOD


n, k = map(int,input().split())
e = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
 
colored = [False]*n
colored[0] = True
num = len(e[0])
ans = perm(k, 1+num)
d = deque()
for i in e[0]:
    colored[i] = True
    d.append(i)
while d:
    f = d.pop()
    num = len(e[f]) - 1
    if num == 0:
        continue
    ans *= perm(k-2, num)
    ans %= MOD
    for i in e[f]:
        if not colored[i]:
            colored[i] = True
            d.appendleft(i)
print(ans % MOD)
