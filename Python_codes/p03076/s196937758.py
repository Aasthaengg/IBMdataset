from itertools import permutations

A = [int(input()) for _ in range(5)]

MIN=10**9
for p in permutations(A):
  SUM=0
  for i in range(5):
    if i < 4:
      SUM += (p[i]+10-1)//10*10
    if i == 4:
      SUM += p[i]
  if SUM < MIN:
    MIN = SUM
    
print(MIN)