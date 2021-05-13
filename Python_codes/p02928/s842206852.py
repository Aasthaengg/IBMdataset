def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    mod = 10 ** 9 + 7

    ans = 0
    for i in range(N):
        tmp_1 = 0
        tmp_2 = 0
        for j in range(N):
            if A[i] > A[j]:
                tmp_1 += 1
            if A[i] > A[j] and i < j:
                tmp_2 += 1

        ans += tmp_2 * K * (K+1) // 2
        ans += (tmp_1-tmp_2) * (K-1) * K // 2
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
