n,k = map(int,input().split())
h = list(map(int,input().split()))
dp = [0] * n
t = []
 
for i in range(1,n):
    for l in range(1,k+1):
        if i - l >= 0:
            t.append(abs(h[i] - h[i-l]) + dp[i-l])
        else:
            break
    dp[i] = min(t)
    t.clear()
 
print(dp[-1])