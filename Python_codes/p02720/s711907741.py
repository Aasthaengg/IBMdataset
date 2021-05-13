from collections import deque

k = int(input())
q = deque(range(1, 10))

for _ in range(k - 1):
    x = q.popleft()
    m = x % 10
    if m != 0:
        q.append(x * 10 + m - 1)
    q.append(x * 10 + m)
    if m != 9:
        q.append(x * 10 + m + 1)

ans = q.popleft()
print(ans)