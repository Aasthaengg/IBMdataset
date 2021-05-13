import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from math import gcd

    n, m = map(int, readline().split())
    s = input()
    t = input()

    d = dict()
    l = (n * m) // gcd(n, m)
    ls = l // n
    lt = l // m

    for i in range(n):
        d[i*ls] = s[i]

    for i in range(m):
        if d.get(i*lt):
            if d[i*lt] != t[i]:
                return print(-1)

    print(l)

if __name__ == '__main__':
    main()
