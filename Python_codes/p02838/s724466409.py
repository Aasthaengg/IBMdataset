import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    ans = 0
    for i in range(60):
        s = 0
        for a in A:
            if a & (1 << i):
                s += 1
        tmp = 0
        for j in range(N):
            if A[j] & (1 << i):
                s -= 1
                tmp += (N - j - 1) - s
            else:
                tmp += s
        ans = (ans + tmp * pow(2, i, MOD)) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
