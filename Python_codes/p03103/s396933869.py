n,m=map(int,input().split())
ab=sorted([list(map(int,input().split())) for _ in range(n)])
ans=0
i=0
while i<n:
    if m>=ab[i][1]:
        ans+=(ab[i][0])*ab[i][1]
        m-=ab[i][1]
        i+=1
    else:
        ans+=(ab[i][0])*(m)
        break
print(ans)