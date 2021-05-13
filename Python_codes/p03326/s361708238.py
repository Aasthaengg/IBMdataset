N, M = map(int, input().split())
cakes = [[] for i in range(N)]
for i in range(N):
    cakes[i] = list(map(int, input().split()))

def calc(c):
    x, y, z = 0, 0, 0
    for i in range(M):
        x += c[i][0]
        y += c[i][1]
        z += c[i][2]
    return abs(x) + abs(y) + abs(z)

ans = 0
for i in (-1, 1):
    for j in (-1, 1):
        for k in (-1, 1):
            cakes.sort(key=lambda x: x[0]*i + x[1]*j + x[2]*k)
            ans = max(ans, calc(cakes))

print(ans)
