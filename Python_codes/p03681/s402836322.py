def factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % 1000000007
    return ans


N, M = map(int, input().split())

MAD = 10**9+7
if abs(N-M) >= 2:
    print(0)

elif N == M:
    print((2*factorial(N)*factorial(M)) % MAD)

else:
    print((factorial(N)*factorial(M)) % MAD)
