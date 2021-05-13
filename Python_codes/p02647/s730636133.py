N, K = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(min(K, 50)):
    B = [0 for k in range(N)]
    for i in range(N):
        l = max(0, i - A[i])
        r = min(N - 1, i + A[i])
        B[l] += 1
        if r + 1 < N:
            B[r+1] -= 1
    # 累積和
    for i in range(1, N):
        B[i] += B[i-1]
    A = B.copy()
   
for b in B:
    print(b, end=" ")