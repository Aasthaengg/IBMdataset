x=int(input())
ans=1
for i in range(2,10):
    for j in range(1,32):
        if j**i<=x:
            ans=max(ans,j**i)
print(ans)