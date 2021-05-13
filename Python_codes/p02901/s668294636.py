from functools import reduce
INF = 10 ** 7
N, M = map(int, input().split())
L = 1 << N
table = [INF] * L
table[0] = 0
for m in range(M):
    cost, _ = map(int, input().split())
    match = reduce(lambda a, b: a | b, (1 << shamt for shamt in map(lambda n: int(n) - 1, input().split())))
    for l in range(L):
        now = table[l]
        if l and not now:
            continue
        table[l | match] = min(now + cost, table[l | match])
print(table[L - 1] if table[L - 1] != INF else -1)