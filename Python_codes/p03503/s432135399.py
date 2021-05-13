n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -10**9
for i in range(1, pow(2, 10)):
    res = 0
    for j in range(n):
        cnt = 0
        for k in range(10):
            if (i >> k)&1 and f[j][k]:
                cnt += 1
        res += p[j][cnt]
    ans = max(ans, res)
print(ans)