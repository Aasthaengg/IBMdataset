import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    T, A = map(int, readline().split())
    H = list(map(int, readline().split()))
    X = map(lambda x: abs(A - (T - 0.006 * x)), H)

    x_min = INF
    ans = -1

    for i, x in enumerate(X, 1):
        if x < x_min:
            ans = i
            x_min = x

    print(ans)


if __name__ == '__main__':
    main()
