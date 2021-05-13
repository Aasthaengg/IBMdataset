n=int(input())
l=list(map(int,input().split()))
dp=[0,abs(l[1]-l[0])]
for i in range(2,n):
    dp.append(min(dp[i-1]+abs(l[i]-l[i-1]),dp[i-2]+abs(l[i]-l[i-2])))
print(dp[-1])