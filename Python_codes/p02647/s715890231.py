def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))  # 整数のリスト
    B = [0] * N

    for j in range(min(K, 41)):
        for i in range(N):
            l = max(0, i-A[i])
            r = min(N-1, i+A[i])
            B[l] += 1
            if r+1 < N: B[r+1] -= 1
        for i in range(1,N):
            B[i] += B[i-1]
        A = B
        B = [0] * N

    for i in A:
        print(i, end=" ")

if __name__ == '__main__':
    main()
