N, K = map(int, input().split())

a = N // K
b = N % K
ans = a ** 3

for i in range(1, K):
    if (2 * (K - i)) % K == 0:
        if i > b:
            if K - i > b:
                ans += a ** 3
            else:
                ans += a * ((a+1)**2)
        else:
            if K - i > b:
                ans += (a + 1) * (a ** 2)
            else:
                ans += (a + 1) ** 3

print(ans)
