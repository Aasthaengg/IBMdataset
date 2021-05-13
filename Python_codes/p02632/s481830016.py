# coding: utf-8
import sys

stdin = sys.stdin
ns = lambda: stdin.readline().rstrip() # ignore trailing spaces
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))


def main():
    k = ni()
    s = ns()
    n = len(s)
    mod = 1000000007
    ans = 0
    inv25 = pow(25, mod-2, mod)
    tmp1 = 1
    tmp2 = pow(25,n+k,mod)
    for m in range(n):
        ans += (tmp1*tmp2)%mod
        ans %= mod
        tmp1 *= (n+k-m)*pow(m+1,mod-2,mod)
        tmp2 *= inv25
        tmp1 %= mod
        tmp2 %= mod
    ans = pow(26,n+k,mod) - ans
    ans %= mod
    print(ans)
    return


if __name__ == '__main__':
    main()