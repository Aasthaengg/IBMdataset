n, k = map(int, input().split())
p = sorted([tuple(map(int, input().split())) for i in range(n)])
ans = 4 * 10**18
for i in range(k, n + 1):
    for j in range(n - i + 1):  # x座標に関して j から i + j まで含む
        x = p[i + j - 1][0] - p[j][0]
        s = sorted([p[a][1] for a in range(j, i + j)])
        y = min(s[a + k - 1] - s[a] for a in range(i - k + 1))
        ans = min(ans, x * y)
print(ans)
