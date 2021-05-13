import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    B = [False] * (N + 1)

    for i, a in reversed(list(enumerate(A, 1))):
        tmp = 0
        for j in range(2 * i, N + 1, i):
            tmp += B[j]
        B[i] = tmp % 2 != a

    ans = [i for i in range(1, N + 1) if B[i]]
    print(len(ans))
    if len(ans) > 0:
        print(' '.join(map(str, ans)))

    return


if __name__ == '__main__':
    main()
