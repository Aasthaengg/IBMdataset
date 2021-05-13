import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())

    x = 0
    cur = 0
    while cur < n:
        x += 1
        cur += x

    if cur == n:
        print("Yes")
        k = x + 1
        res = [[0] * x for _ in range(x + 1)]

        for i in range(1, x + 1):
            l = i * (i - 1) // 2 + 1
            for j in range(i):
                res[j][i - 1] = j + l
            for j in range(i):
                res[i][j] = j + l
        print(k)
        for row in res:
            print(k - 1, *row)
    else:
        print("No")


if __name__ == '__main__':
    main()
