n = int(input())

MOD = 1000000000 + 7

ans = 1
for i in range(n):
    ans *= i + 1
    ans %= MOD

print(ans)
