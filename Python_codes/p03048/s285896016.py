R, G, B, N = map(int, input().split())

ans = 0
b = 0
for r in range(N+1):
    for g in range(N+1):
        b = (N - r*R - g*G)//B
        if r*R + g*G + b*B == N and b >= 0:
            ans += 1
print(ans)