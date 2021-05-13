from collections import deque
n = int(input())
a = list(map(int, input().split()))

ans = deque([])
t = 0
for i in a:
  if t == 0: ans.append(i)
  else: ans.appendleft(i)
  t = 1 - t

if t == 0: print(*ans)
else: print(*reversed(ans))