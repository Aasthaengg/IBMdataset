N = int(input())
mod = 10**9 + 7

dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(N+1)]
dp[0][3][3][3] = 1
let = {i:l for i,l in enumerate('AGCT')}

for i in range(1,N+1):
    for l3 in range(4):
        for l2 in range(4):
            for l1 in range(4):
                for nextl in range(4):
                    flag = True
                    for j in range(4):
                        lets = list(let[l3]+let[l2]+let[l1]+let[nextl])
                        if j >= 1:
                            lets[j-1],lets[j] = lets[j],lets[j-1]
                        if 'AGC' in ''.join(lets):
                            flag = False
                            break
                    if flag:
                        dp[i][l2][l1][nextl] += dp[i-1][l3][l2][l1]
                        dp[i][l2][l1][nextl] %= mod
ans = 0
for l3 in range(4):
    for l2 in range(4):
        for l1 in range(4):
            ans = (ans + dp[N][l3][l2][l1])%mod
print(ans)
