N,M = map(int, input().split())
A = [int(a) for a in input().split()]

data = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
inf = -10**9
dp = [inf for i in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    for j in range(M):
        if i-data[A[j]] >= 0:
            dp[i] = max(dp[i], dp[i-data[A[j]]]+1)
            
ans = 0
A.sort(reverse=True)
n = dp[N]
i = n-1
temp = N
while i >= 0:
    j = 0
    while j < M:
        if temp-data[A[j]] >= 0:
            if dp[temp-data[A[j]]] == dp[temp]-1:
                temp -= data[A[j]]
                temp = max(temp, 0)
                ans += A[j]*10**i
                j = M
        j += 1
    i -= 1
    
print(ans)