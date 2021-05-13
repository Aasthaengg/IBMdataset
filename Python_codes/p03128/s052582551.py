import sys
input = lambda: sys.stdin.readline().rstrip()

match_dict = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

N,M = map(int, input().split())
A = list(map(int, input().split()))

#桁数のMAX
dp = [-1] * (N+1)
dp[0] = 0

for a in A:
    for i in range(match_dict[a], N+1):
        if dp[i - match_dict[a]] >= 0:
            dp[i] = max(dp[i], dp[i - match_dict[a]] + 1)

ans = ''
A.sort(reverse=True)

i = N
while i:
    for a in A:
        if i - match_dict[a] >= 0 and dp[i - match_dict[a]] == dp[i] - 1:
            ans += str(a)
            i -= match_dict[a]
            break

print(ans)