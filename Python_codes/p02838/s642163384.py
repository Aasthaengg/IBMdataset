import sys

read = sys.stdin.buffer.read
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    M = 60

    ans = 0
    p = 1
    for d in range(M):
        n = 0
        for i in range(N):
            if A[i] & (1 << d):
                n += 1
        ans = (ans + n * (N - n) * p) % MOD
        p = p * 2 % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
