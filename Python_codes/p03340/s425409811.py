n=int(input())
A=[int(i) for i in input().split()]
ans=0
l,r=0,0
x,s=A[0],A[0]
while l!=n-1 or r!=n-1:
  if x==s:
    ans+=r-l+1
    if r<n-1:
      r+=1
      x^=A[r]
      s+=A[r]
    else:
      break
  else:
    l+=1
    x^=A[l-1]
    s-=A[l-1]
if l==n-1 and r==n-1:
  ans+=1
print(ans)