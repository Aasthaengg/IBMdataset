
from collections import deque

K = int(input())
q = deque(list(range(1, 10)))
cnt = 0
ans = 0
while True:
    u = q.popleft()
    cnt += 1
    if cnt == K:
        ans = u
        break

    ll = u % 10
    for i in range(max(0, ll - 1), min(9, ll + 1) + 1):
        q.append(u * 10 + i)

print(ans)
