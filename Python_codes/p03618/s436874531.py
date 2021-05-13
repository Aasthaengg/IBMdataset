from collections import Counter

A = input()
C = Counter(A)

n = len(A)
minus = 0
for v in C.values():
  minus += v*(v-1)//2
  
print(1 + n*(n-1)//2 - minus)