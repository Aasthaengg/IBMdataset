x=list(map(int,input().split()))

ans=1
for i in range(5):
    if x[i]==0:
        print(ans)
    else:
        ans+=1