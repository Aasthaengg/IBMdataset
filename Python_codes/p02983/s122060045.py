L,R=map(int,input().split())

ans=2018
i=L
while i<R:
    j=i+1
    while j<=R:
        if i*j%2019==0:
            ans=0
            break
        else:
            ans=min(ans,i*j%2019)
            j+=1
    i+=1
    if ans==0:
        break

print(ans)