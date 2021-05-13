import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate

    n, m = map(int, readline().split())
    c = [0] * n

    for i in range(m):
        a, b = map(int, readline().split())
        a, b = a - 1, b - 1
        a, b = min(a, b), max(a, b)
        c[a] += 1
        c[b] -= 1

    d = list(accumulate(c))

    if all((x % 2 == 0 for x in d)):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
