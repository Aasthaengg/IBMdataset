all_match = [2,5,5,4,5,6,3,7,6]

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
match = []
for num in a:
    match.append(all_match[num-1])

dp = [-10**7 for i in range(n+1)] #桁数
dp[0] = 0

for i in range(1,n+1):
    possible = []
    for honsu in match:
        if i >= honsu:
            possible.append(dp[i-honsu] + 1)
    if len(possible)>0:
        dp[i] = max(possible)

length = dp[n]
ans = 0
now = n
for i in range(length):
    for j in range(m):
        if now >= match[j]:
            if dp[now-match[j]] == dp[now]-1:
                ans += a[j]*10**(length-i-1)
                now -= match[j]
                break

print(ans)