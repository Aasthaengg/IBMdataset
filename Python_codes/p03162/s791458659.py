#dpは拡張されたdpテーブルでdp[i][j]はi日目にjの活動を選択したときに取れる最大の満足度
n = int(input())
dp = [[0]*3]*(n)
an = list(map(int,input().split()))
dp[0] = an
for i in range(1,n):
    
    a,b,c = list(map(int, input().split()))
    
    
    a_m = max(dp[i-1][1]+a, dp[i-1][2]+a)
    b_m = max(dp[i-1][0]+b, dp[i-1][2]+b)
    c_m = max(dp[i-1][0]+c, dp[i-1][1]+c) 
    dp[i] = [a_m,b_m,c_m]

print(max(dp[-1][:]))