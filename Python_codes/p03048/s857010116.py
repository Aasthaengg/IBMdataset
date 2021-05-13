R, G, B, N = map(int, input().split())
ans = 0
for r in range(N+1):
    for g in range(N+1):
        temp = N - r*R - g*G
        if temp < 0:
            continue
        if temp%B == 0:
            ans += 1
print(ans)
