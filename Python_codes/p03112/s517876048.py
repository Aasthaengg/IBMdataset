import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
A, B, Q = map(int, input().split())
a = [-10 ** 18] + [int(input()) for _ in range(A)] + [10 ** 18]
b = [-10 ** 18] + [int(input()) for _ in range(B)] + [10 ** 18]
for _ in range(Q):
  x = int(input())
  ra = bl(a, x)
  rb = bl(b, x)
  la = ra - 1
  lb = rb - 1
  res = 10 ** 18
  res = min(res, max(abs(a[ra] - x), abs(b[rb] - x)))
  res = min(res, max(abs(a[la] - x), abs(b[lb] - x)))
  res = min(res, max(abs(a[la] - x), abs(b[rb] - x)) + min(abs(a[la] - x), abs(b[rb] - x)) * 2)
  res = min(res, max(abs(a[ra] - x), abs(b[lb] - x)) + min(abs(a[ra] - x), abs(b[lb] - x)) * 2)
  print(res)