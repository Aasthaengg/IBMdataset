import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B, X = map(int, readline().split())

    if A <= X <= A + B:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
