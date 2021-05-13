h, w, k = map(int, input().split())
MOD = 10**9+7
memo = [[0]*(w+1) for _ in range(h+1)]
dp = [[1]*2 for _ in range(w+1)]
dp[0][0] = 0
for i in range(2, w+1):
    for j in range(2):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
#print(dp)
def poss_of_ok_spaces(idx,straight):
    if straight:
        ok_spaces_l = max(idx - 1 - 1, 0)
        ok_spaces_r = max(w - idx - 1, 0)
        return sum(dp[ok_spaces_l])%MOD * sum(dp[ok_spaces_r])%MOD
    else:
        #右の数値を飛ばす前提
        ok_spaces_l = max(idx - 1 - 2, 0)
        ok_spaces_r = max(w - idx - 1, 0)
        return sum(dp[ok_spaces_l])%MOD * sum(dp[ok_spaces_r])%MOD

def rc(n,idx):
    if memo[n][idx] != 0:
        return memo[n][idx]
    if n == 1:
        if idx == k:
            return poss_of_ok_spaces(idx,True)%MOD
        elif k == idx + 1:
            return poss_of_ok_spaces(k,False)%MOD
        elif k == idx - 1:
            return poss_of_ok_spaces(idx,False)%MOD
        else:
            return 0
    ret = rc(n-1,idx)%MOD*poss_of_ok_spaces(idx,True)%MOD
    if idx + 1 <= w:
        ret += rc(n-1,idx+1)%MOD*poss_of_ok_spaces(idx+1,False)%MOD
    if idx - 1 >= 1:
        ret += rc(n-1,idx-1)%MOD*poss_of_ok_spaces(idx,False)%MOD
    ret %= MOD
    memo[n][idx] = ret
    return ret
print(rc(h,1))