from collections import deque

N = int(input())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    to[a - 1].append(b - 1)
    to[b - 1].append(a - 1)
dist = None
pars = [0] * N
q = deque()
q.append((0, 0, 0))
while len(q):
    a, d, p = q.pop()
    pars[a] = p
    if a == N - 1:
        dist = d
        break
    for b in to[a]:
        if b != p:
            q.append((b, d + 1, a))

boundw = N - 1
for _ in range((dist - 1) // 2):
    boundw = pars[boundw]

q = deque()
q.append((0, 1, 0))
ans = 0
while len(q):
    a, sgn, p = q.pop()
    if a == boundw:
        sgn = -1
    ans += sgn
    for b in to[a]:
        if b != p:
            q.append((b, sgn, a))
print("Fennec" if ans > 0 else "Snuke")
