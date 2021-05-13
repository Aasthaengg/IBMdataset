n=int(input())
ans=9999999999999
for i in range(1,int(n/2)+1):
  tempa=list(str(i))
  tempb=list(str(n-i))
  s=0
  for j in range(len(tempa)):
    s=s+int(tempa[j])
  for j in range(len(tempb)):
    s=s+int(tempb[j])
  ans=min(ans,s)
print(ans)
