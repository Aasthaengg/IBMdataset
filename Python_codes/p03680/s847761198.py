import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    seq = []

    for _ in range(N):
        a = int(readline())
        a -= 1
        seq.append(a)

    cur = 0

    for i in range(1, 10 ** 6):
        cur = seq[cur]
        if cur == 1:
            return print(i)

    print(-1)


if __name__ == '__main__':
    main()
