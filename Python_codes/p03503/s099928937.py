N = int(input())
F = tuple(tuple(map(int, input().split())) for _ in range(N))
P = tuple(tuple(map(int, input().split())) for _ in range(N))
ans = -float("inf")
for n in range(1, 1024):
    indices = [0] * N
    for i in range(N):
        for j in range(10):
            if (n >> (9 - j)) & 1:
                indices[i] += F[i][j]
    ans = max(ans, sum(profit[idx] for profit, idx in zip(P, indices)))
print(ans)