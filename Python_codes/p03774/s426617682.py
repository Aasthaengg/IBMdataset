N, M = map(int, input().split())

As = []
for _ in range(0, N):
    x, y = input().split()
    As.append((int(x), int(y)))

Cs = []
for _ in range(0, M):
    x, y = input().split()
    Cs.append((int(x), int(y)))

for a in As:
    d = {}
    minI = -1
    minM = float('inf')
    for i, c in enumerate(Cs):
        ax, ay = a
        cx, cy = c
        m = abs(ax - cx) + abs(ay - cy)
        if m < minM:
            minI = i + 1
            minM = m

    print(minI)
