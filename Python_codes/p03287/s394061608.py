from itertools import accumulate
from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
L = [0] + list(accumulate(A))
L = [ i%m for i in L ]
C = Counter(L)
ans = 0
for i in C.values():
  ans += i*(i-1)//2
print(ans)