from math import sqrt, gcd
import sys


def osk_a(M):
    p = [i for i in range(M+1)]
    for x in range(2, int(sqrt(M))+1):
        if p[x] == x:
            for y in range(2*x, M+1, x):
                if p[y] == y:
                    p[y] = x
    return p


def main():
    n = int(sys.stdin.buffer.readline())
    a = list(map(int, sys.stdin.buffer.readline().split()))

    def g(a):
        g = 0
        for x in a:
            g = gcd(g, x)
        return g

    if g(a) > 1:
        print("not coprime")
        exit()
    p = osk_a(10**6)
    chk = set()
    while a[0] > 1:
        chk.add(p[a[0]])
        a[0] //= p[a[0]]
    for x in a[1:]:
        tmp = set()
        while x > 1:
            tmp.add(p[x])
            x //= p[x]
        if not chk.isdisjoint(tmp):
            print("setwise coprime")
            exit()
        chk |= tmp
    print("pairwise coprime")


if __name__ == "__main__":
    main()
