import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, a, b = map(int, readline().split())
    h = [0] * n
    for i in range(n):
        h[i] = int(readline())

    ok = 10 ** 18
    ng = 0

    c = a - b

    while abs(ng - ok) > 1:
        mid = (ng + ok) >> 1
        cnt = 0
        for x in h:
            if x > mid * b:
                cnt += (x - mid * b + c - 1) // c
        if cnt <= mid:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == '__main__':
    main()
