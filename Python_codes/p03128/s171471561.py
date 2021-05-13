N, M = map(int, input().split())
A = list(map(int, input().split()))
num = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

dp = [0]*(N+1)
INF = -float('inf')

for i in range(1, N+1):
    dp[i] = max([dp[i-num[j]] if i - num[j] >= 0 else INF for j in A]) + 1

A.sort(reverse = True)
ans = ''
tmp = N
while tmp > 0:
    for a in A:
        if tmp-num[a] >=0:
            if dp[tmp-num[a]] == dp[tmp] - 1:
                break
    ans += str(a)
    tmp -= num[a]
    
print(ans)    