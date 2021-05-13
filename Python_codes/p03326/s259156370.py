N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for bit in range(1 << 3):
    scores = [0] * N
    for i in range(N):
        for j in range(3):
            scores[i] += xyz[i][j] * (-1)**((bit >> j) & 1)
    scores.sort(reverse=True)
    ans = max(ans, sum(scores[:M]))
print(ans)
