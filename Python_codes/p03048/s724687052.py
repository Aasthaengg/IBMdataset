R, G, B, N = map(int, input().split())

ans = 0
for r in range(N//R + 1):
    n = N - R*r
    for g in range(n//G + 1):
        if (n - G*g) % B == 0:
            ans += 1
print(ans)
