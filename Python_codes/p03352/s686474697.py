x=int(input())
ans=0
for i in range(2,10):
    for j in range(1,1001):
        tmp=j**i
        if tmp<=x:
            ans=max(tmp,ans)
print(ans)