R, G, B, N = map(int, input().split())

ans = 0
for r in range(N // R + 1):
    rest = N - r * R
    ans += sum((rest - g * G) % B == 0 for g in range (rest // G + 1))

print(ans)