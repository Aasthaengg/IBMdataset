from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import defaultdict
from bisect import *

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

N = read()
A = sorted(reads())
B = sorted(reads())
C = sorted(reads())

numB = [0] * N
for i in range(N):
  numB[i] = N - bisect_left(C, B[i]+1)
print(numB, file=stderr)

anumB = [0] * (N+1)
for i in range(N):
  anumB[i+1] = anumB[i] + numB[i]
print(anumB, file=stderr)

numA = [0] * N
for i in range(N):
  numA[i] = anumB[N] - anumB[bisect_left(B, A[i]+1)]
print(numA, file=stderr)

print(sum(numA))