a,b,c,d=map(int,input().split())
ab=list([a,b])
cd=list([c,d])
ans=ab[0]*cd[0]
for i in range(len(ab)):
    for j in range(len(cd)):
        temp=ab[i]*cd[j]
        ans=max(ans,temp)
print(ans)