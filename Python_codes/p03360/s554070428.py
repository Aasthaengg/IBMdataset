import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = list(map(int, readline().split()))
    K = int(readline())
    x.sort(reverse=True)

    ans = x[0] * 2 ** K + x[1] + x[2]
    print(ans)


if __name__ == '__main__':
    main()
