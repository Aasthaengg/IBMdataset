R, G, B, N = map(int, input().split())
R, G, B = sorted([R, G, B], reverse=True)
maxR = N // R
ans = 0
if R == 1:
    ans = (N+2)*(N+1) // 2
    print(ans)
    quit()

for r in range(maxR+1):
    if r * R == N:
        ans += 1
        continue
    n = N - r * R
    maxG = n // G
    for g in range(maxG+1):
        if g * G == n:
            ans += 1
            continue
        nn = n - g * G
        maxB = nn // B
        for b in range(maxB+1):
            if b * B == nn:
                ans += 1

print(ans)