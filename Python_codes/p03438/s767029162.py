import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    b = list(map(int, readline().split()))

    cnt = 0
    for x, y in zip(a, b):
        diff = x - y
        if diff < 0:
            cnt += abs(diff) // 2

    for x, y in zip(a, b):
        diff = x - y
        if diff > 0:
            cnt -= diff

    if cnt >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
