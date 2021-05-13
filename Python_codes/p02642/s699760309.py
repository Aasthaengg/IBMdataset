n=int(input())
a=list(map(int,input().split()))
a.sort()
dp=[0]*(a[-1]+1)

for i in a :
    dp[i]+=1

for i in a :
    if dp[i] :
        for j in range(i*2,a[-1]+1,i) :
            dp[j]=0

print(dp.count(1))
