from functools import reduce
INF = 10 ** 7
N, M = map(int, input().split())
L = 1 << N
keys = [0] * M
for m in range(M):
    cost, _ = map(int, input().split())
    match = reduce(lambda a, b: a | b, (1 << shamt for shamt in map(lambda n: int(n) - 1, input().split())))
    keys[m] = cost, match
table = [[INF] * L for _ in range(M + 1)]
table[0][0] = 0
for m in range(M):
    cost, match = keys[m]
    for l in range(L):
        now = table[m][l]
        if l and not now:
            continue
        table[m + 1][l] = min(now, table[m + 1][l])
        table[m + 1][l | match] = min(now + cost, table[m + 1][l | match])
print(table[M][L - 1] if table[M][L - 1] != INF else -1)