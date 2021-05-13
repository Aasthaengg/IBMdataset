def get_dp(dp,h,n):
    for i in range(1,n,1):
        if i == 1:
            tmp1 = abs(h[i] - h[i-1])
            dp[i] = tmp1
        else:
            tmp1 = abs(h[i] - h[i-1]) + dp[i-1]
            tmp2 = abs(h[i] - h[i-2]) + dp[i-2]
            dp[i] = min(tmp1,tmp2)

    return dp[n-1]

def main():
    n = int(input())
    h = list(map(int,input().split()))
    dp = [0]*(n)
    print(get_dp(dp,h,n))

main()
