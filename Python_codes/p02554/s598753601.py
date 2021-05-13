#!/usr/bin/env python3

import sys

input = iter(sys.stdin.read().splitlines()).__next__

MOD = 1000000007

def powmod(x, n):
   if n == 0: return 1
   if (n % 2) == 1:
      return (powmod((x*x) % MOD, n//2) * x) % MOD
   else:
      return powmod((x*x) % MOD, n//2)

N = int(input())

total = powmod(10, N)

#print(total)

cnt_without0 = powmod(9, N)
cnt_without9 = cnt_without0
cnt_without0nor9 =  powmod(8, N)

res = (total - cnt_without0 - cnt_without9 + cnt_without0nor9) % MOD
if res < 0:
   res += MOD

print(res)

