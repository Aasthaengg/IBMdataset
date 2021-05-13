from collections import deque
N, D, A = map(int, input().split())
XH = []
for _ in range(N):
    x, h = map(int, input().split())
    XH.append((x, h))
XH.sort(key=lambda x: x[0])
D = 2 * D
tot = 0
q = deque()
ans = 0
for i in range(N):
    x, h = XH[i]
    while 0 < len(q) and q[0][0] < x:
        tot -= q[0][1]
        q.popleft()
    h -= tot
    if h > 0:
        num = (h + A - 1) // A
        ans += num
        damage = num * A
        tot += damage
        q.append((x + D, damage))
print(ans)
