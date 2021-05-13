N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [False]*(K+1)
for i in range(1,K+1):
    for a in A:
        if i-a >= 0 and dp[i-a] == False:
            dp[i] = True
            break
print("First" if dp[-1] else "Second")
