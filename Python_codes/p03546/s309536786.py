H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
d = {i: 0 for i in range(-1, 10)}
for _ in range(H):
    A = map(int, input().split())
    for i in A:
        d[i] += 1
ans = 0
for i in range(10):
    if i == 1:
        continue
    ans += c[i][1] * d[i]
print(ans)
