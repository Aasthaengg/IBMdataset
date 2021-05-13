from collections import deque
n = int(input())

dp = [-1 for _ in range(10**6)]
dp[0] = 0

que = deque([0])

while que:
    v = que.popleft()
    j6 = 1
    while v+j6 <= n:
        if dp[v+j6] == -1:
            dp[v+j6] = dp[v]+1
            que.append(v+j6)
        j6 *= 6
            
    j9 = 1
    while v+j9 <= n:
        if dp[v+j9] == -1:
            dp[v+j9] = dp[v]+1
            que.append(v+j9)
        j9 *= 9
            
print(dp[n])