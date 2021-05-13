R, G, B, N = map(int, input().split())
ans = 0
for i in range(N + 1):
    r = i * R
    if r > N:
        break
    for j in range(N + 1):
        g = j * G
        if r + g > N:
            break
        b = N - r - g
        if b >= 0 and b % B == 0:
            ans += 1
print(ans)
