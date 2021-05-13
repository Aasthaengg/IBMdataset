import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, C, X = map(int, read().split())

    ans = 0
    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                if 500 * i + 100 * j + 50 * k == X:
                    ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
