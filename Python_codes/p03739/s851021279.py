import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    b = [0] * n
    c = [0] * n

    score1 = 0
    cur = 0
    for i, x in enumerate(a):
        if i % 2 == 0:
            nx = x + cur
            if nx <= 0:
                diff = abs(nx) + 1
                score1 += diff
                cur = 1
            else:
                cur = nx
        else:
            nx = x + cur
            if nx >= 0:
                diff = abs(nx) + 1
                score1 += diff
                cur = -1
            else:
                cur = nx

    score2 = 0
    cur = 0
    for i, x in enumerate(a):
        if i % 2 == 1:
            nx = x + cur
            if nx <= 0:
                diff = abs(nx) + 1
                score2 += diff
                cur = 1
            else:
                cur = nx
        else:
            nx = x + cur
            if nx >= 0:
                diff = abs(nx) + 1
                score2 += diff
                cur = -1
            else:
                cur = nx

    print(min(score1, score2))


if __name__ == '__main__':
    main()
