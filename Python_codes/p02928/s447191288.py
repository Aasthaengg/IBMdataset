MOD = 10 ** 9 + 7

if __name__ == "__main__":
    N, K = [int(x) for x in input().split(" ")]
    A = [int(x) for x in input().split(" ")]

    count_a = 0
    count_b = 0
    A_ = K * (K + 1) // 2
    B = K * (K - 1) // 2
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] > A[j]:
                count_a += 1
            if A[i] < A[j]:
                count_b += 1

    print((A_ * count_a + B * count_b) % MOD)