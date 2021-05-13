import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def main():
    s = int(readline())

    d = dict()

    a = s
    d[a] = 1
    for i in range(2, 10000000):
        a = f(a)
        if a in d:
            ans = i
            break
        else:
            d[a] = i

    print(ans)
    return


if __name__ == '__main__':
    main()
