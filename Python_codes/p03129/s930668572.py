n,k=map(int,input().split())
ans="NO"
if n%2==1:
  if n>2*(k-1):
    ans="YES"
else:
  if n>=2*k:
    ans="YES"
print(ans)