def sol(lis,K):
    import sys
    dp = [sys.maxsize]*len(lis)
    dp[0] = 0
    for i in range(len(lis)):
        for j in range(i+1,i+K+1):
            if j<len(lis):
                dp[j] = min(dp[j],dp[i]+abs(lis[j]-lis[i]))
    print(dp[-1])
n,k = list(map(int,input().split(' ')))
lis = list(map(int,input().split(' ')))
sol(lis,k)