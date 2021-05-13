from collections import Counter
n = int(input())
A = list(map(int, input().split()))
a = A[0]
for i in range(1, n):
  a ^= A[i]
c = Counter(A)
if a == 0:
  if len(c) == 3 and all(v == n // 3 for v in c.values()):
    print('Yes')
  elif len(c) == 2 and c.get(0) > 0 and n - c[0] == 2 * c[0]: 
    print('Yes')
  elif len(c) == 1 and c.get(0) == n:
    print('Yes')
  else:
    print('No')
else:
  print('No')