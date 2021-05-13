N = int(input())
C = [int(input()) for _ in range(N)]

l = sorted([(c, i) for i,c in enumerate(C)])

path = [[i+1] for i in range(N)]

for i in range(len(l)-1):
    if l[i][0] == l[i+1][0] and l[i+1][1]-l[i][1] > 1:
        path[l[i][1]].append(l[i+1][1])

dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(N-1):
    for to in path[i]:
        dp[to] = (dp[to]+dp[i])%1000000007

print(dp[N-1])
