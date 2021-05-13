R, G, B, N = [int(_) for _ in input().split()]

ans = 0
for i in range(N // R + 1):
    M = N - i * R
    for j in range(M // G + 1):
        X = M - j * G
        if X % B == 0:
            ans += 1
print(ans)
