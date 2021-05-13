from bisect import bisect
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

BC_ruiseki = deque([0])
for i, b in enumerate(B):
  BC_ruiseki.append(BC_ruiseki[i] + N - bisect(C, b))

ans = 0
for a in A:
  idx = bisect(B, a)
  ans += BC_ruiseki[-1] - BC_ruiseki[idx]
print(ans)