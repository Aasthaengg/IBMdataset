n = int(input())
mod = int(1e9 + 7)
ans = 0
if n <= 1:
    print(ans)
else :
    ans = pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)
    ans += 2 * mod
    ans %= mod
    print(ans)