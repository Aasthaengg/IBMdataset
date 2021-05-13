n, m = map(int, input().split())

MOD = 10 ** 9 + 7

if n == m:
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % MOD
    print(ans * ans * 2 % MOD)

elif n + 1 == m:
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i % MOD
    print(ans * ans * m % MOD)

elif n == m + 1:
    ans = 1
    for i in range(2, m + 1):
        ans = ans * i % MOD
    print(ans * ans * n % MOD)

else:
    print(0)