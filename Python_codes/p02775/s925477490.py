n=list(map(int,list(input())))

#右からi桁目、繰り上げあり1、繰り上げ無し0
dp=[[0]*2 for _ in range(len(n)+1)]

nrev=n[::-1]
nrev.append(0)
dp[0][0]=nrev[0]
dp[0][1]=10-nrev[0]
#print(0,dp)
for i in range(1,len(n)+1):
    dp[i][0]=min(dp[i-1][0]+nrev[i],dp[i-1][1]+(nrev[i]+1))
    dp[i][1]=min(dp[i-1][0]+(10-nrev[i]),dp[i-1][1]+(10-(nrev[i]+1)))
    #print(i,nrev[i],dp)

print(min(dp[-1]))


        

