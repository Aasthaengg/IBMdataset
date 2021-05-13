N, M = map(int, input().split())
A = list(map(int, input().split()))


COST = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}
A = sorted(A, reverse=True)

best = [None for _ in range(N + 1)]
best[0] = tuple([0] * len(A))
for n in range(N + 1):
    for ai, a in enumerate(A):
        before = n - COST[a]
        if before < 0 or best[before] is None:
            continue
        val = tuple(x + (1 if i == ai else 0) for i, x in enumerate(best[before]))
        if (
            best[n] is None
            or sum(best[n]) < sum(val)
            or (sum(best[n]) == sum(val) and best[n] < val)
        ):
            best[n] = val
print(''.join(sorted(''.join(str(d) * n for d, n in zip(A, best[N])), reverse=True)))