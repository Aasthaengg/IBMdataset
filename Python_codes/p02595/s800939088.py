n, d = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    p = ls[i][0]
    q = ls[i][1]
    if (p ** 2 + q ** 2) ** 0.5 <= d:
        ans += 1

print(ans)