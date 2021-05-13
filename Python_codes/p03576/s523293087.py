n, k = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(n)]
f.sort()
ans = 1145141919810893364364
for i in range(n - k + 1):
    for j in range(i + k - 1, n):
        a = [f[l][1] for l in range(i, j + 1)]
        a.sort()
        for l in range(j - i - k + 2):
            ans = min(ans, (f[j][0] - f[i][0]) * (a[l + k - 1] - a[l]))
print(ans)