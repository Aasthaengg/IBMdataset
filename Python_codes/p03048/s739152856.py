R, G, B, N = map(int, input().split())
ans = 0

for r in range(min(3000, 3000 // R) + 1):
    if R * r <= N:
        for g in range(min(3000, 3000 // G) + 1):
            v = R * r + G * g
            if N >= v and (N - v) % B == 0:
                ans += 1

print(ans)
