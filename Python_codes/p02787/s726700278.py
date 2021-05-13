[H,N] = list(map(int,input().split()))
AB = []
for i in range(N):
    AB.append(list(map(int,input().split())))

dp = [0]*(H+1)
inf = float('inf')

for i in range(1,H+1):
    ans = inf
    for j in range(N):
        A = AB[j][0]
        B = AB[j][1]
        if i>=A:
            cand = dp[i-A]+B
        else:
            cand = B
        if cand<ans:
            ans=cand
    dp[i] = ans

print(dp[-1])