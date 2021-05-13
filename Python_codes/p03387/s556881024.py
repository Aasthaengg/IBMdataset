a,b,c=sorted(map(int,input().split()))
ans=0
if a==b==c:
  ans=0
else:
  ans+=c-b
  if (b-a)%2==0:
    ans+=(b-a)//2
  else:
    ans+=(b-a+3)//2
print(ans)