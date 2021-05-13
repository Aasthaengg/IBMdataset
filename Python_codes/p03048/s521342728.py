R, G, B, N = map(int, input().split())

ans = 0
for r in range(0, 3001):
    for g in range(0, 3001):
        if (N - r * R - g * G) // B >= 0 and (N - r * R - g * G) % B == 0:
            ans += 1
print(ans)
