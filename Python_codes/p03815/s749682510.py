x=int(input())
y=19

ans=0
ans+=(x//11)*2
cnt=x%11
if cnt>=7:
  ans+=2
elif cnt>=1:
  ans+=1
  
print(ans)