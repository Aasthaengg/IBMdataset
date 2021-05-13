n=int(input())

ab=[list(map(int,input().split())) for i in range(n)]

c=[]
ans=0
if ab[n-1][0]%ab[n-1][1]!=0:   
    ans+=ab[n-1][1]-(ab[n-1][0]%ab[n-1][1])
#print(ab[n-1][0],ab[n-1][1],ans)
for i in range(n-2,-1,-1):
    ab[i][0]+=ans
    if ab[i][0]%ab[i][1]!=0:
        
        ans+=ab[i][1]-(ab[i][0]%ab[i][1])
    #print(ab[i][0],ab[i][1],ans)
print(ans)