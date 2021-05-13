N = int(input())
mod = 10**9 + 7

dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(N+1)]
dp[0][3][3][3] = 1
let = {i:l for i,l in enumerate('AGCT')}

def judge(lets):
    for i in range(4):
        t = lets.copy()
        if i >= 1:
            t[i-1],t[i] = t[i],t[i-1]
        if 'AGC' in ''.join(t):
            return False
    return True

for i in range(1,N+1):
    for l3 in range(4):
        for l2 in range(4):
            for l1 in range(4):
                for nextl in range(4):
                    lets = list(let[l3]+let[l2]+let[l1]+let[nextl])
                    if judge(lets):
                        dp[i][l2][l1][nextl] += dp[i-1][l3][l2][l1]
                        dp[i][l2][l1][nextl] %= mod
ans = 0
for l3 in range(4):
    for l2 in range(4):
        for l1 in range(4):
            ans = (ans + dp[N][l3][l2][l1])%mod
print(ans)
