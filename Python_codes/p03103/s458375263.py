n, m = map(int, input().split())
ab = sorted([tuple(map(int, input().split())) for i in range(n)])
i, ans = 0, 0
while ab[i][1] < m:
    m -= ab[i][1]
    ans += ab[i][1] * ab[i][0]
    i += 1
ans += ab[i][0] * m
print(ans)