import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, A, *H = map(int, read().split())

    diff = INF
    for i, h in enumerate(H, 1):
        if diff > abs(T - h * 0.006 - A):
            diff = abs(T - h * 0.006 - A)
            ans = i

    print(ans)
    return


if __name__ == '__main__':
    main()
