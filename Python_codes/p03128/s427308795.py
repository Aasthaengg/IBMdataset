m = [0,2,5,5,4,5,6,3,7,6]

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(len(A)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if m[A[i]] == m[A[j]]:
            del A[i]
            break

dp = [-1] * (N+1)
dp[0] = 0

for i in range(N):
    if dp[i]==-1: continue
    for j in range(len(A)):
        ind = i + m[A[j]]
        if ind <= N:
            dp[ind] = max(dp[ind], dp[i] * 10 + A[j])

print(dp[-1])
