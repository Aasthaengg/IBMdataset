import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, k = map(int, readline().split())
    res = dict()
    cnt = 0

    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            cnt += 1
            res[cnt] = i

    num = (cnt + 1) - k
    print(res[num])


if __name__ == '__main__':
    main()
