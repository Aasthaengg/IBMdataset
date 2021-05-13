import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    k = int(readline())
    a = list(map(int, readline().split()))
    a = a[::-1]

    if a[0] != 2:
        return print(-1)

    l = 2
    r = 3

    for x in a[1:]:
        l = (x + l - 1) // x * x
        r = r // x * x + (x - 1)

    if l == r == 0 or l > r:
        print(-1)
    else:
        print(l, r)


if __name__ == '__main__':
    main()
