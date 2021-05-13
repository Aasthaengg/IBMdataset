import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H, N = map(int, readline().split())
    A = list(map(int, readline().split()))

    if sum(A) >= H:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
