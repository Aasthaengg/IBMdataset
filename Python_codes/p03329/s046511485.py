N = int(input())

def calc_dp(n):
    initial = 10**7
    dp=[initial for _ in range(100100)]#dp用の配列はすこし大きめに作る
    dp[0] = 0

    for i in range(100001):
        count = 0
        while 6**count <= n:
            power_six = 6**count
            count += 1
            if i - power_six >= 0:
                dp[i] = min(dp[i],1 + dp[i-power_six])
                
        count = 1
        while 9**count <= n:
            power_nine = 9**count
            count += 1
            if i - power_nine >= 0:
                dp[i] = min(dp[i],1 + dp[i-power_nine])

    return dp[n]

print(calc_dp(N))
