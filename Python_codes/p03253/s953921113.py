import sys
import collections


def alg_duplicate_combination_mod(n, r, mod):
    n = n + r - 1
    r = min(n - r, r)
    if r == 0:
        return 1
    else:
        denominator = 1
        for i in range(n, n - r, -1):
            denominator = (denominator * i) % mod
        molecule = 1
        for i in range(1, r + 1):
            molecule = (molecule * i) % mod
        return denominator * pow(molecule, mod - 2, mod) % mod


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    ls = []
    for i in range(2, int(m ** 0.5) + 1):
        while True:
            if m % i == 0:
                ls.append(i)
                m //= i
            else:
                break
    if m != 1:
        ls.append(m)
    t = 1
    ls = collections.Counter(ls)
    for k, v in ls.items():
        t *= alg_duplicate_combination_mod(n, v, mod)
        t %= mod
    print(t)


if __name__ == '__main__':
    solve()
