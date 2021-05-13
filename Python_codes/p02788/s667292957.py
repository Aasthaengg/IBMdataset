from collections import deque
n, d, a = map(int, input().split())
xh = [list(map(int, input().split())) for i in range(n)]
xh.sort()
que = deque()
ans = 0
atk = 0
for x, h in xh:
    while que and que[0][0] <= x:
        atk -= que.popleft()[1]
    h -= a*atk
    if h <= 0:
        continue
    count = -(-h//a)
    ans += count
    atk += count
    que.append((x+2*d+1, count))
print(ans)