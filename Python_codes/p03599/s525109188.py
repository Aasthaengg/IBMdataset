a, b, c, d, e, f = map(int, input().split())
dp = [[False] * 3001 for _ in range(3001)]
dp[0][0] = True
satomizumax = 0
satomax = 0
for sm in range(f + 1):
    for sg in range(f + 1):
        # // 4toori
        # sg/sm <= e/(100+e)
        if sg * (100 + e) > e * sm:
            break

        if dp[sm][sg]:
            if satomax * sm <= sg * satomizumax:
                satomizumax = sm
                satomax = sg
            if sm + 100 * a <= f + 1:
                dp[sm + 100 * a][sg] = True
            if sm + 100 * b <= f + 1:
                dp[sm + 100 * b][sg] = True
            if sm + c <= f + 1 and sg + c <= f + 1:
                dp[sm + c][sg + c] = True
            if sm + d <= f + 1 and sg + d <= f + 1:
                dp[sm + d][sg + d] = True
print(satomizumax, satomax)
