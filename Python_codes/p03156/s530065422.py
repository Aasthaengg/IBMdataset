import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A, B = map(int, readline().split())
    P = list(map(int, readline().split()))

    cnt = [0] * 3

    for x in P:
        if x <= A:
            cnt[0] += 1
        elif x <= B:
            cnt[1] += 1
        else:
            cnt[2] += 1

    print(min(cnt))


if __name__ == '__main__':
    main()
