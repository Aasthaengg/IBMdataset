n,m=map(int,input().split())
s=str(input())
s=list(s)
t=str(input())
t=list(t)
ans=-1
if s[0]==t[0]:
  import fractions
  temp=len(s)*len(t)//fractions.gcd(len(s),len(t))
  k=fractions.gcd(len(s),len(t))
  count=1
  for i in range(1,k):
    if s[i*int(len(s)/k)]==t[i*int(len(t)/k)]:
      count=count+1
  if count==k:
    ans=temp
print(ans)
