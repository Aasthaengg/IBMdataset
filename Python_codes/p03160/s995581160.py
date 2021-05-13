n=int(input())
h=[int(i) for i in input().split()]

dp=[]
dp.append(0)
dp.append(abs(h[1]-h[0]))
for i in range(2,n):
    x=min(dp[i-2]+abs(h[i]-h[i-2]),dp[i-1]+abs(h[i]-h[i-1]))
    dp.append(x)
print(dp[-1])
