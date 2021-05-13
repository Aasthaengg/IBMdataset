import itertools


def solve():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    cntA, cntB = 0, 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                cntA += 1
        for j in range(N):
            if A[i] > A[j]:
                cntB += 1

    M = 10**9 + 7
    # オーバーフロー対策で掛け算毎に剰余をとる
    a = cntA * K % M
    b = ((K - 1) * K // 2) % M * cntB % M
    print((a + b) % M)


if __name__ == '__main__':
    solve()