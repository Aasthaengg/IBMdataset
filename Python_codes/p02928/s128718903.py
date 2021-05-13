import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    cnt = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                cnt += 1
    cnt_1 = 0
    for i in range(N):
        for j in range(N):
            if A[i] > A[j]:
                cnt_1 += 1
    a = cnt * K % MOD
    b = (cnt_1 * K * (K - 1) // 2) % MOD
    answer = (a + b) % MOD
    print(answer)


if __name__ == "__main__":
    main()
