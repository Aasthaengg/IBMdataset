N = int(input())
S = [input() for _ in range(N)]

from collections import Counter
C = Counter(S)

maxC = max(C.values())

A=[]
for k,v in C.items():
  # print(k,v)
  if v==maxC: A.append(k)

A = sorted(A)

for a in A:
  print(a)

