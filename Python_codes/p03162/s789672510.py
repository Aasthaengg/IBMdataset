am = int(input())
val = [[0]*(am+5),[0]*(am+5),[0]*(am+5)]
dp = [[0]*(am+5),[0]*(am+5),[0]*(am+5)]
for i in range(am):
    A,B,C = list(map(int,input().split()))
    val[0][i] = A
    val[1][i] = B
    val[2][i] = C

for i in range(0,am):
    for g in range(3):
        for j in range(3):
            if g!=j:
                dp[g][i+1] = max(dp[g][i+1],dp[j][i]+val[g][i])

print(max(dp[0][am],dp[1][am],dp[2][am]))