s=input()
t=s.replace('x','')
n=len(t)
if not(n==1 or t[:n//2]==t[(n+1)//2:][::-1]):
  print(-1)
  exit()
n=len(s)
r=n-1
l=0
ans=0
while r>l:
  nr,nl=r,l
  while s[r]=='x' and r>0:r-=1
  while s[l]=='x' and l<n-1:l+=1
  ans+=abs(nr-r+nl-l)
  while s[r]==s[l] and l<r:
    r-=1
    l+=1
print(ans)