import math
N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]

def check(k):
  cnt = 0
  for i in range(N):
    cnt += max(0, math.ceil((h[i] - B*k) / (A - B)))
  if cnt <= k:
    return 1
  else:
    return 0

y, n = 10**10, 0
while y-n > 1:
  k = (y+n)//2
  if check(k):
    y = k
  else:
    n = k

print(y)
