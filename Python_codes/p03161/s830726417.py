INF = 10**10

def chmax(a, b):
    if(a>b):
        return a
    else:
        return b

def chmin(a, b):
    if(a<b):
        return a
    else:
        return b


N, K = map(int,input().split())

h = list(map(int,input().split()))

dp = N*[INF]
dp[0]=0


for i in range(1,N):
    for j in range(1,K+1):
        dp[i] = chmin(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
        if i < j:
            break

#print(dp)
print(dp[N-1])