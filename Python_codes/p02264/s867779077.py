from collections import deque
n, q = map(int, input().split())
f = lambda a, b: (a, int(b))
dq = deque(f(*input().split()) for _ in range(n))
ans = 0
li = []
while dq:
    s, t = dq.popleft()
    if t <= q:
        ans += t
        li.append(s + " " + str(ans))
    else:
        ans += q
        dq.append((s, t - q))
print(*li, sep="\n")

