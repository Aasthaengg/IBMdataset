
from collections import Counter
N = int(input())
A = [int(input()) for _ in range(N)]
ca = Counter(A)

ans = 0
for v in ca.values():
  if v%2:
    ans += 1
print(ans)