N,K = map(int, input().split())
A = [int(a) for a in input().split()]

dp = [False]*(K+1)

for i in range(K+1):
    f = False
    for j in range(N):
        if A[j] > i:
            break
        if dp[i-A[j]]:
            continue
        f = True
    dp[i] = f
    
if dp[K]:
    ans = "First"
else:
    ans = "Second"
        
print(ans)