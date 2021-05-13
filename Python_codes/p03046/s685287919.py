import sys
import time

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    m, k = list(map(int, readline().split()))

    if m == 0:
        if k == 0:
            print(0, 0)
        else:
            print(-1)
    elif m == 1:
        if k == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
    else:
        if k < 2 ** m:
            x = [i for i in range(2 ** m)]
            x.remove(k)
            y = x[::-1]
            ans = x + [k] + y + [k]
            print(*ans)
        else:
            print(-1)


if __name__ == '__main__':
    main()
