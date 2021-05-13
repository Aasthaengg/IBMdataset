N, M = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(2 ** 3):
    F = [1, 1, 1]
    for j in range(3):
        if ((i >> j) & 1):
            F[j] = -1

    s = []
    for x, y, z in C:
        s.append(x*F[0]+y*F[1]+z*F[2])
    s = sorted(s, reverse=True)

    ans = max(ans, sum(s[:M]))
print(ans)
