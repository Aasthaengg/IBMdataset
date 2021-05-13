N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
assert len(P) == N
assert len(Q) == N

import itertools
a = 0
b = 0
for i,nums in enumerate(itertools.permutations(range(1,N+1))):
  if list(nums) == P:
    a = i
  if list(nums) == Q:
    b = i
print(abs(b - a))