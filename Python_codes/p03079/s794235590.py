from sys import stdin
A, B, C = [int(_) for _ in stdin.readline().rstrip().split()]
if A == B == C:
  print('Yes')
else:
  print('No')