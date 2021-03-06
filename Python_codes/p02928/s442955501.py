def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    MOD = 10**9 + 7
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] == A[j]:
                continue
            elif A[i] > A[j]:
                count += K + K*(K-1) // 2
            else:
                k = K - 1
                count += k + k*(k-1) // 2
        count %= MOD

    print(count)
    



main()