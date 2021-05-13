N, K = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(K):
    if len(set(A)) == 1 and A[0] == N:
        break
    work = [0] * (N + 1)
    for i in range(N):
        a = A[i]
        idx0 = max(0, i - a)
        idx1 = min(N, i + a + 1)
        work[idx0] += 1
        work[idx1] -= 1
    now = 0
    for i in range(N):
        now += work[i]
        A[i] = now
print(*A)