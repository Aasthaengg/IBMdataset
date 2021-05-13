from collections import deque
N, K = map(int, input().split())
ans = (N // K)**3
if K % 2 == 0:
  m = K // 2
  cnt = 0
  i = m
  while i <= N:
    i += K
    cnt += 1
  ans += cnt**3
print(ans)