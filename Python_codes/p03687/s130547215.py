s=str(input())
l=len(s)
ans=99999999999
for j in s:
  temp=j
  a=0
  cnt=0
  for i in range(l):
    if s[i]!=temp:
      cnt=cnt+1
    else:
      a=max(a,cnt)
      cnt=0
  a=max(a,cnt)
  ans=min(a,ans)
print(ans)