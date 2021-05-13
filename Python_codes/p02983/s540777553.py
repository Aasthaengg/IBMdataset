import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    L, R = map(int, readline().split())

    if R - L > 3000:
        print(0)
    else:
        A = [i % 2019 for i in range(L, R + 1)]
        ans = INF
        for i in range(R - L):
            for j in range(i + 1, R - L + 1):
                ans = min(ans, A[i] * A[j] % 2019)
        print(ans)

    return


if __name__ == '__main__':
    main()
