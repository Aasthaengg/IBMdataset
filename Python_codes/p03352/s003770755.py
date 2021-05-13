x=int(input())
ans=1
for i in range(1,1000+1):
    for j in range(2,11):
        if i**j<=x:
            ans=max(ans,i**j)

print(ans)