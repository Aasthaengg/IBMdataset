N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [0 for _ in range(N+1)]
cnt = 0
while min(A) < N and cnt < K:
    cnt += 1
    for i in range(N):
        L[max(i-A[i], 0)] += 1
        L[min(i+A[i]+1, N)] -= 1
    for i in range(N):
        L[i+1] += L[i]
        A[i] = L[i]
        L[i] = 0
for i in range(N):
    print(A[i], end = ' '*(i!=N-1))