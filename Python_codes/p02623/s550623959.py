def solve():
    sum_A = [0 for _ in range(N + 1)]
    sum_B = [0 for _ in range(M + 1)]

    for i in range(1, N + 1):
        sum_A[i] = sum_A[i-1] + A[i-1]

    for i in range(1, M + 1):
        sum_B[i] = sum_B[i-1] + B[i-1]

    ans = 0
    j = M
    for i in range(N + 1):
        if sum_A[i] > K:
            break

        while sum_B[j] > K - sum_A[i]:
            j -= 1

        ans = max(ans, i + j)

    print(ans)

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solve()