N,M=map(int,input().split())
keys=[]
dp=[float("inf")]*pow(2,N)
dp[0]=0
for i in range(M):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    num=0
    for j in l:
        num=num+pow(2,j-1)
    keys.append([a,num])
#print(keys)
for i in range(pow(2,N)):
    for j in range(M):
        dp[i|keys[j][1]]=min(dp[i|keys[j][1]],dp[i]+keys[j][0])
    #print(dp)
#print(dp)
if dp[pow(2,N)-1]==float("inf"):
    print(-1)
else:
    print(dp[pow(2,N)-1])