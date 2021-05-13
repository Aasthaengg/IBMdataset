from bisect import bisect_right
N = int(input())
L = {1}
m = 6
n = 9
while m <= N:
    L.add(m)
    m *= 6
while n <= N:
    L.add(n)
    n *= 9
L = list(L)
L.sort()
# print(L)

dp = [N]*(N+1)
dp[0] = 0

for i in range(1, N+1):
    x = bisect_right(L, i)
    for j in range(x):
        dp[i] = min(dp[i], dp[i-L[j]]+1)

# print(dp)
print(dp[N])
