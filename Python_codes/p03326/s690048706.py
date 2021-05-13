import itertools

N, M = map(int, input().split())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for xs, ys, zs in itertools.product([1, -1], repeat=3):
    S = sorted([(xs * x + ys * y + zs * z) for x, y, z in XYZ], reverse=True)
    ans = max(ans, sum(S[:M]))
print(ans)
