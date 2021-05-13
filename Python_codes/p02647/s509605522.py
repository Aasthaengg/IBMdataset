N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = [0] * (N+1)

for j in range(K):
    ans = [0] * (N+1)
    for i in range(N):
        L = max(0, i-A[i])
        R = min(N, i+A[i]+1)
        ans[L] += 1
        ans[R] -= 1
    for i in range(1, N+1):
        ans[i] += ans[i-1]
    issame = True
    for i in range(N):
        if i != 0:
            if ans[i-1] != N or ans[i-1] != ans[i]:
                issame = False
        A[i] = ans[i]
    if issame:
        break

for i in range(N):
    print(ans[i], end=' ')