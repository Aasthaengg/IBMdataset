import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    n = int(readline())
    d = list(map(int, readline().split()))
    m = int(readline())
    t = list(map(int, readline().split()))

    cd = Counter(d)
    ct = Counter(t)

    cd.subtract(ct)

    for key, val in cd.items():
        if val < 0:
            return print("NO")

    print("YES")


if __name__ == '__main__':
    main()
