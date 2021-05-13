N, M = map(int, input().split())
cake = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for bit in range(8):
    u = 1 if (bit >> 0) & 1 else -1
    v = 1 if (bit >> 1) & 1 else -1
    w = 1 if (bit >> 2) & 1 else -1
    A = []
    for (x, y, z) in cake:
        A.append(x * u + y * v + z * w)
    A.sort(reverse=True)
    ans = max(ans, sum(A[:M]))

print(ans)
