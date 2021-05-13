n, m = map(int, input().split())
s = input()

from collections import deque
q = deque()

pre = [-1] * (n+1)
f = [float('inf')] * (n +1)
f[0] = 0

q.append((f[0], 0))
for i in range(1, n+1):
  while q and i - q[0][1] > m:
    q.popleft()
  if s[i] == '1': continue
  if q:
    f[i] = q[0][0] + 1
    pre[i] = q[0][1]
  while q and q[-1][0] > f[i]:
    q.pop()
  if f[i] != float('inf'):
    q.append((f[i], i))

if pre[n] == -1:
  print(-1)
else:
  now = n
  res = [n]
  while pre[now] != -1:
    now = pre[now]
    res.append(now)
  res = res[::-1]
  ans = [y -x for x, y in zip(res, res[1:])]
  print(*ans)
