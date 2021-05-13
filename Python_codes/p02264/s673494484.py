from collections import deque
n, q = map(int, input().split())
f = lambda a, b: (a, int(b))
dq = deque(f(*input().split()) for _ in range(n))
cnt = 0
ans = []
while dq:
    s, t = dq.popleft()
    if t <= q:
        cnt += t
        ans.append(f"{s} {cnt}")
    else:
        cnt += q
        dq.append((s, t - q))
print(*ans, sep="\n")

