import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def sum_arithmetic_seq(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2

def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7

    B = [0] * N
    C = [0] * N
    for i in range(N):
        for j in range(i):
            if A[i] < A[j]:
                B[i] += 1
    for i in range(N):
        for j in range(N):
            if A[i] < A[j]:
                C[i] += 1

    ans = sum(B) * K
    ans %= MOD
    ans += sum_arithmetic_seq(0, sum(C), K)
    ans %= MOD
    print(ans)



if __name__ == '__main__':
    main()
