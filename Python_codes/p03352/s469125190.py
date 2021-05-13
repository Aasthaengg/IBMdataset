x=int(input())
ans=1
for num in range(2,x+1):
    k=x
    cnt=0
    while k>=num:
        k//=num
        cnt+=1
    if cnt>=2:
        ans=max(ans,pow(num,cnt))
print(ans)