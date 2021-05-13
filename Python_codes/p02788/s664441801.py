import math
from collections import deque
N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for _ in range(N)]
XH = sorted(XH)
total = 0
D = 2*D
ans = 0
q = deque()
for x, h in XH:
  while len(q) and q[0][0] < x:
    total -= q.popleft()[1] 
  h -= total

  if h > 0:
    num = math.ceil(h/A)
    ans += num
    damage = num*A
    total += damage
    q += [[x+D, damage]]
print(ans)
