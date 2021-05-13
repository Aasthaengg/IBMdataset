import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = [int(readline()) for _ in range(n)]
    idx = {}

    for i, x in enumerate(a):
        idx[x] = i

    mx = 1
    cnt = 1
    for x in range(1, n):
        if idx[x] < idx[x + 1]:
            cnt += 1
            mx = max(mx, cnt)
        else:
            cnt = 1

    print(n - mx)


if __name__ == '__main__':
    main()
