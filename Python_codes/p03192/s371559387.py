n=int(input())
ans=0
while n>0:
    if n%10==2:
        ans+=1
    n=n//10
print(ans)