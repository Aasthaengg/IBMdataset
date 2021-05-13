R, G, B, N = map(int, input().split())
mr, mg, mb = N//R, N//G, N//B

ans = 0
for r in range(mr+1):
    for g in range(mg+1):
        val = N - r*R - g*G
        if val >= 0 and val % B == 0:
            ans += 1
print(ans)