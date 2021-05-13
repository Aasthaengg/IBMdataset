# C Tax Increase

from math import ceil

A, B = map(int, input().split())

a = [i for i in range(ceil(A*100/8), int((A+1)*100/8))]
b = [i for i in range(B*10, (B+1)*10)]

ans = list(set(a) & set(b))
if ans:
  print(min(ans))
else:
  print(-1)