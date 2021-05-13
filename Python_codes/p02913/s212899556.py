import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    s = input()
    x = 1

    sn = [ord(c) - 96 + x for c in s]

    lmax = n // 2
    m1 = 10 ** 9 + 7
    m2 = 2 ** 61 - 1

    ans = 0

    ng = n + 1
    ok = 0

    while abs(ng - ok) > 1:
        l = (ng + ok) // 2
        found = False

        appeared = set()
        diff = pow(m1, l - 1, m2)

        h_init = 0

        for i in range(l):
            h_init += sn[i] * pow(m1, l - 1 - i, m2)
            h_init %= m2

        hashlist = [0] * n
        hashlist[l - 1] = h_init
        h = h_init

        for i in range(l, n):
            h -= sn[i - l] * diff
            h *= m1
            h += sn[i]
            h %= m2
            hashlist[i] = h
            if i - l >= 0:
                appeared.add(hashlist[i - l])
            if h in appeared:
                found = True
                break

        if found:
            ok = l
        else:
            ng = l

    print(ok)


if __name__ == '__main__':
    main()
