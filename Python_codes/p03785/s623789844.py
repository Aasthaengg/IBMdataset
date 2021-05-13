from collections import deque

n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]

t.sort()

q = deque(t)
cnt = 1
ans = 1
curr = q.popleft()

while q:
    tmp = q.popleft()
    if tmp - curr <= k and cnt < c:
        cnt += 1
    else:
        ans += 1
        cnt = 1
        curr = tmp

print(ans)