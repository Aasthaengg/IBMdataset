import sys
readline = sys.stdin.readline

N = int(readline())
P = tuple(map(int,readline().split()))
Q = tuple(map(int,readline().split()))

import itertools
a = 0
b = 0
cnt = 0
for perm in itertools.permutations(range(1, N + 1)):
  cnt += 1
  if perm == P:
    a = cnt
  if perm == Q:
    b = cnt
    
print(abs(a - b))    