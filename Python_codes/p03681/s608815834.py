MOD = int(1e9) + 7

def f(n):
    ans = 1

    for i in range(2, n + 1):
        ans = (ans * i) % MOD

    return ans

n, m = map(int, input().split())

if abs(n - m) > 1:
    print(0)

    exit()

ans = (f(n) * f(m)) % MOD

if n == m:
    ans = (ans * 2) % MOD

print(ans)
