N, M = map(int, input().split())

S, C = [], []
for _ in range(N):
    a, b = map(int, input().split())
    S.append((a, b))

for _ in range(M):
    c, d = map(int, input().split())
    C.append((c, d))

for a, b in S:
    ans = None
    min_dist = 1 << 32
    for i, (c, d) in enumerate(C):
        dist = abs(c - a) + abs(d - b)
        if dist < min_dist:
            min_dist = dist
            ans = i
    print(ans + 1)