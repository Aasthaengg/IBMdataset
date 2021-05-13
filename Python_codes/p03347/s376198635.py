from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import bisect, bisect_left

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

N = read()

A = []
for _ in range(N):
  A.append(read())

if A[0] != 0 or not all(A[i-1] >= A[i] - 1 for i in range(1, N)):
  print(-1)
  exit()

S = sorted(set(i - A[i] for i in range(N)))
print('S:', S, file=stderr)

ans = 0
for i in range(N):
  x = bisect_left(S, i) - bisect_left(S, i - A[i])
  print(i, x, file=stderr)
  ans += x
print(ans)
