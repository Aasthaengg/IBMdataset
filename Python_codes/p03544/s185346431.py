import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    res = [2, 1]

    for i in range(100):
        cur = res[i] + res[i + 1]
        res.append(cur)

    print(res[N])


if __name__ == '__main__':
    main()
