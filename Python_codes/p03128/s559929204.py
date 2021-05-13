Q = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}
 
N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
 
# 桁数の最大
dp = [-1] * (N + 1)
dp[0] = 0
 
for a in A:
    for i in range(Q[a], N + 1):
        if dp[i - Q[a]] >= 0:
            dp[i] = max(dp[i], dp[i - Q[a]] + 1)
            #print(dp)
 
# 整数の復元
ans = ''
 
# 大きな数から試す
A.sort(reverse=True)
 
i = N
while i:
    for a in A:
        if i - Q[a] >= 0 and dp[i - Q[a]] == dp[i] - 1:
            ans += str(a)
            i -= Q[a]
            break
 
print(ans)