import math
from bisect import bisect_left as bl
from itertools import accumulate

n,h = map(int,input().split())
A = []
B = []
ans = 0

for _ in range(n):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

A.sort(reverse=1)
B.sort()

index = bl(B, A[0])
B = B[index:]
B = list(accumulate(B[::-1]))
if B[-1] >= h:
  print(bl(B,h)+1)
  exit()
  
h -= B[-1]
ans += len(B)
ans += math.ceil(h/A[0])
print(ans)