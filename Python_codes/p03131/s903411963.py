k,a,b=map(int,input().split())
ans=1
if a+2>=b or a>=k:
  ans=k+1
else:
  k-=a-1
  ans+=a-1
  ans+=(k//2)*(b-a)
  if k%2==1:
    ans+=1
print(ans)

