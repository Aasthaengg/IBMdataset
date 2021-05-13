def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    mod = 10 ** 9 + 7
    for i in range(N):
        left = 0
        for j in range(i):
            if A[j] < A[i]:
                left += 1
        right = 0
        for j in range(i+1, N):
            if A[j] < A[i]:
                right += 1
        ans += (right * K * (K+1) + left * (K-1) * K) // 2
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()