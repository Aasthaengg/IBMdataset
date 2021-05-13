n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
for j in range(n):
    ans = 0
    for k in range(m):
        if ab[k][0] == j + 1:
            ans += 1
        elif ab[k][1] == j + 1:
            ans += 1
    print(ans)