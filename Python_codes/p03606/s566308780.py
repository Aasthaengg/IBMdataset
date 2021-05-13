import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    seq = [False] * 100000

    for _ in range(N):
        l, r = map(int, readline().split())
        l -= 1
        for i in range(l, r):
            seq[i] = True

    print(seq.count(True))


if __name__ == '__main__':
    main()
