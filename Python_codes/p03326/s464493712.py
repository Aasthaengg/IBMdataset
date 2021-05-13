import itertools

N, M = map(int, input().split())
cakes = []
for _ in range(N):
    cakes.append(tuple(map(int, input().split())))

ans = 0
for t in itertools.product([1, -1], repeat=3):
    tmp = [sum(cakes[i][j] * t[j] for j in range(3)) for i in range(N)]
    ans = max(ans, sum(sorted(tmp, reverse=True)[:M]))
print(ans)