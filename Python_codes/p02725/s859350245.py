K, N = map(int, input().split())
A = list(map(int, input().split()))
if N == 2:
    print(min(A[1]-A[0], K-A[1]+A[0]))
else:
    ans = K - A[N-1] + A[0]
    for i in range(N-1):
        ans = max(A[i+1]-A[i], ans)
    print(K - ans)