N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = [0] * 8
for bit in range(2 ** 3):
    cand = [0] * N
    for i in range(N):
        for j in range(3):
            cand[i] += [1, -1][bit >> j & 1] * X[i][j]

    cand = sorted(enumerate(cand), key=lambda x: -x[1])
    res = [0] * 3
    for i, _ in cand[:M]:
        for j in range(3):
            res[j] += X[i][j]
    ans[bit] = sum(map(abs, res))

print(max(ans))
