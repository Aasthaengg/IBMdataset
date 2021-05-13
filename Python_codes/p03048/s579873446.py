R, G, B, N = map(int, input().split())
ans = 0
for r in range(N // R + 1):
    for g in range(N // G + 1):
        b = N - r * R - g * G
        if b < 0 or b % B != 0:
            continue
        ans += 1
print(ans)