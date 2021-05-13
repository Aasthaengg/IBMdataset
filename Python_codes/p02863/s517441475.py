n, t = map(int, input().split())
dishes = [tuple(map(int, input().split())) for _ in range(n)]

t -= 1
dp1 = [[0] * (t+1) for _ in range(n+1)]
dp2 = [[0] * (t+1) for _ in range(n+2)]

# from top
for i in range(n):
    for time in range(t+1):
        if time - dishes[i][0] >= 0:
            dp1[i+1][time] = max(
                dp1[i][time-dishes[i][0]] + dishes[i][1],
                dp1[i][time]
            )
        dp1[i+1][time] = max(dp1[i][time], dp1[i+1][time])


for j in reversed(range(2, n+2)):
    i = j-2
    for time in range(t+1):
        if time - dishes[i][0] >= 0:
            dp2[j-1][time] = max(
                dp2[j][time-dishes[i][0]] + dishes[i][1],
                dp2[j][time]
            )
        dp2[j-1][time] = max(dp2[j][time], dp2[j-1][time])


ans = 0
for i in range(1, n+1):
    for time in range(t+1):
        ans = max(
            ans,
            dp1[i-1][time] + dishes[i-1][1] + dp2[i+1][t - time]
        )
print(ans)