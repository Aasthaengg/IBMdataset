N, M = map(int, input().split())

Cakes = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(1 << 3):
    Cake = [0] * N
    for j in range(3):
        if (i >> j) & 1 == 1:
            for c in range(N):
                Cake[c] += Cakes[c][j]
        else:
            for c in range(N):
                Cake[c] -= Cakes[c][j]
    Cake.sort(reverse=True)
    ans = max(ans, sum(Cake[:M]))


print(ans)
