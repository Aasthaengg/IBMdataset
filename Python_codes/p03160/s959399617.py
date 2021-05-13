N=int(input())
h=list(map(int, input().split()))

# dpの最小値を変更する関数
def chmin(a, b):
    if a > b:
        return b
    else:
        return a
      
dp=[0]*N
dp[1]=abs(h[1]-h[0])

for i in range(2,N):
    tmp=chmin(abs(h[i]-h[i-1])+dp[i-1],abs(h[i]-h[i-2])+dp[i-2])
    dp[i]=tmp
    
print(dp[-1])