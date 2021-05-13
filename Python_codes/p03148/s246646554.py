N , K = map(int, input().split())
sushi = [list(map(int, input().split())) for i in range(N)]
top = [-10**10]*(N+1)
sub = [0]
cnt = 0
for t, d in sushi:
    if top[t] < d:
        sub.append(top[t])
        top[t] = d
    else:
        sub.append(d)
top.sort(reverse = True)
sub.sort(reverse = True)
top_dp = [0] *(N+1)
sub_dp = [0] * (N+2)
top_dp[1] = top[0]
sub_dp[1] = sub[0]
for i in range(1, N):
    top_dp[i+1] = top_dp[i] + top[i]
for i in range(1, len(sub)):
    sub_dp[i+1] = sub_dp[i] + sub[i]
dp = [0] * (K+1)
for i in range(1, K+1):
    dp[i] = top_dp[i] + sub_dp[K-i] + i*i
print(max(dp))