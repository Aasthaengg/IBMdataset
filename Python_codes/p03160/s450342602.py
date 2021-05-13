def main():
    n = int(input())
    h_list = list(map(int, input().split()))
 
    dp = [100000]*n
 
    dp[0] = 0
    for i in range(1,n):
 
        tmp_dp1 = 1000000
        tmp_dp2 = 1000000
        if i - 1 >= 0:
            tmp_dp1 = dp[i-1] + abs(h_list[i] - h_list[i-1])
 
        if i - 2 >= 0:
            tmp_dp2 =  dp[i-2] + abs(h_list[i] - h_list[i-2])
        dp[i]=min(tmp_dp1, tmp_dp2)
    print(dp[n-1])
main()