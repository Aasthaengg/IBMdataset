import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())

    for a in range(1, 3501):
        for b in range(1, 3501):
            nu = n * a * b
            dn = 4 * a * b - n * (a + b)
            if dn > 0 and nu % dn == 0:
                return print(a, b, nu // dn)


if __name__ == '__main__':
    main()
