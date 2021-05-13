d=[0,2,5,5,4,5,6,3,7,6]
N,M=map(int,input().split())
A=list(map(int,input().split()))

dp = [-1 for i in range(N+1)]
dp[0] = 0


for i in range(1,N+1):
    tmp = -1
    for a in A:
        if i-d[a]>=0 and dp[i-d[a]] != -1:
            tmp = max(tmp,dp[i-d[a]]+1)
    dp[i] = tmp


A.sort(reverse=True)
ans = ''
while N>0:
    for a in A:
        if N-d[a]>=0 and dp[N-d[a]] == dp[N]-1:
            ans += str(a)
            N -= d[a]
            break
print(ans)



