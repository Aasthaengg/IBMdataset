import itertools

int1 = lambda x: int(x) - 1

H, W, N = map(int, input().split())
B = set(tuple(map(int1, input().split())) for _ in range(N))

adj = (-1, 0, 1)
visited = set()
ans = [0] * 10
for a, b in B:
    for dy, dx in itertools.product(adj, repeat=2):
        if not (1 <= a + dy < H - 1 and 1 <= b + dx < W - 1):
            continue
        elif (a + dy, b + dx) in visited:
            continue
        visited.add((a + dy, b + dx))
        c = 0
        for ddy, ddx in itertools.product(adj, repeat=2):
            if (a + dy + ddy, b + dx + ddx) in B:
                c += 1
        ans[c] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
for x in ans:
    print(x)
