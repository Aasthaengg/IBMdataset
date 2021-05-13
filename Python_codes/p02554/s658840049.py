n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


def modpow(a, n, mod):
    # a^nをmodでわったあまり 二分累乗法O(logn)
    res = 1
    while n > 0:
        if n & 1:
            res = (res*a) % mod
        a = (a*a) % mod
        n = n >> 1
    return res


mod = 10**9 + 7
if n == 1:
    ans = 0
else:
    ans = modpow(10, n, mod)-2*modpow(9, n, mod)+modpow(8, n, mod)
    ans = ans % mod
print(ans)
