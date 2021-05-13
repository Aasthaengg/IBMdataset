n=int(input())
ans=0
if n%10==2:
    ans+=1
if ((n-n%10)/10)%10==2:
    ans+=1
if ((n-n%100)/100)%10==2:
    ans+=1
if (n-n%1000)/1000==2:
    ans+=1
print(ans)