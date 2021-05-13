import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = set(map(int, readline().split()))

    if s == {1, 9, 7, 4}:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
