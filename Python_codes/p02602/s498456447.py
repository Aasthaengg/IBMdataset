N, K = map(int, input().split())
A = list(map(int, input().split()))

score = sum(A[:K])

for i in range(N-K):
    cur = score
    score += A[K+i] - A[i]
    if score > cur:
        print('Yes')
    else:
        print('No')
