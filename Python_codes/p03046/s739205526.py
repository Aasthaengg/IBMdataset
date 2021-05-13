M,K=map(int,input().split())
        
ans=[]
for i in range(pow(2,M)):
    if i!=K:
        ans.append(str(i))
ans1=ans+[str(K)]+ans[::-1]+[str(K)]
if K==0:
    ans1=[]
    for i in range(pow(2,M)):
        ans1+=[str(i)]*2
if K>=pow(2,M):
    print(-1)
elif K==M==1:
    print(-1)
else:
    print(' '.join(ans1))