N = int(input())
h = [int(i) for i in input().split()]

# dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a
      
dp=[1000000000]*N
dp[0]=0
#dp[1]=abs(h[1]-h[0])
 
#配るDP
for i in range(0,N-1):
    #print(abs(h[i]-h[i+1])+dp[i],dp[i+1],abs(h[i]-h[i+2])+dp[i],dp[i+2])
    dp[i+1]=chmin(abs(h[i]-h[i+1])+dp[i],dp[i+1])
    if i < N-2:
        dp[i+2]=chmin(abs(h[i]-h[i+2])+dp[i],dp[i+2])
    
print(dp[-1])
