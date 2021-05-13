K, A, B = map(int, input().split())

if B - A >= 2:
    n_0 = A - 1
    n_1 = (K - n_0) // 2
    ans = 1 + n_1 * (B - A) + (K - 2 * n_1) * 1
else:
    ans = 1 + K

print(ans)