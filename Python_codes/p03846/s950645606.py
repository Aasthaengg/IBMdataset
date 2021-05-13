import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter

    n = int(readline())
    a = list(map(int, readline().split()))
    counter = Counter(a)
    ok = True

    if n % 2 == 1:
        if counter[0] != 1:
            ok = False

        for i in range(2, n, 2):
            if counter[i] != 2:
                ok = False
    else:
        for i in range(1, n, 2):
            if counter[i] != 2:
                ok = False

    if ok:
        print(pow(2, n // 2, MOD))
    else:
        print(0)


if __name__ == '__main__':
    main()
