import bisect
from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()

d = deque([])
for i in range(N):
  n = bisect.bisect_right(C, B[N-1-i])
  if len(d) == 0:
    d.appendleft(N-n)
  else:
    d.appendleft(N-n+d[0])
  
ans = 0
for i in range(N):
  m = bisect.bisect_right(B, A[i])
  if m < N:
    ans += d[m]
print(ans)