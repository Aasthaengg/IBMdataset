N,K = map(int,input().split())
A = list(map(int,input().split()))

dp = [0]*(K+1)
for k in range(1,K+1) :
    for a in A :
        if k-a >= 0 and dp[k-a] == 0 :
            dp[k] = 1

print("First" if dp[K] else "Second")
