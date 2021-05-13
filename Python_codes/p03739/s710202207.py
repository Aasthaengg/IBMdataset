import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
res = max(0, -a[0] + 1)
sm = 1
if a[0] >= 1:
  res = 0
  sm = a[0]
#print(res, sm)
for i in range(1, N):
  if sm > 0:
    res += max(-1, a[i] + sm) + 1
    sm = min(-1, sm + a[i])
  else:
    res += -min(1, sm + a[i]) + 1
    sm = max(1, sm + a[i])
  #print(res, sm)
res2 = max(0, a[0] + 1)
sm = -1
if a[0] <= -1:
  res2 = 0
  sm = a[0]
for i in range(1, N):
  if sm > 0:
    res2 += max(-1, a[i] + sm) + 1
    sm = min(-1, sm + a[i])
  else:
    res2 += -min(1, sm + a[i]) + 1
    sm = max(1, sm + a[i])
  #print(res2, sm)
#print(res, res2)
print(min(res, res2))