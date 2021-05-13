from functools import reduce

N = int(input())
mod = 10**9 + 7


def powmod(val, n, mod):
    # vals = [val]*n
    # ret = reduce(lambda x, y: x * y % mod, vals)

    # return ret

    ret = 1
    for i in range(n):
        ret = ret * val % mod

    return ret


all = powmod(10, N, mod)
b = powmod(9, N, mod)
c = powmod(8, N, mod)

ans = (all - (2*b - c))%mod

print(ans)