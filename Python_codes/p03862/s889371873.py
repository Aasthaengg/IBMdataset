# i番目とi - 1番目の箱の中身の和がxを超えているとき、i番目から余剰分を引く

import sys
readline = sys.stdin.readline

N,x = map(int,readline().split())
A = list(map(int,readline().split()))

ans = 0
if A[0] > x:
  ans += A[0] - x
  A[0] = x

for i in range(1,len(A)):
  if A[i] + A[i - 1] > x:
    diff = (A[i] + A[i - 1]) - x 
    ans += diff
    A[i] -= diff

print(ans)