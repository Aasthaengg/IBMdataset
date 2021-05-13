x, y = map(int, input().split())

n = (2*y - x) // 3
m = (2*x - y) // 3

if (x + y) % 3 != 0 or n < 0 or m < 0:
    print(0)
    exit()


def cmb(n,r):
    mod = 10**9+7
    ans = 1
    for i in range(r):
        ans *= n-i
        ans %= mod
    for i in range(1,r+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    return ans


print(cmb(n+m, n))