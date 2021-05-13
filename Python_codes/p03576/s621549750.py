from itertools import combinations
N, K = map(int, input().split())
dots = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

ans = 10 ** 37
for i in range(N):
    for j in range(i+K-1, N):
        width = dots[j][0] - dots[i][0]
        y = sorted([l for _, l in dots[i:j+1]])
        for a, b in zip(y, y[K-1:]):
            height = b - a
            ans = min(ans, width*height)

print(ans)
