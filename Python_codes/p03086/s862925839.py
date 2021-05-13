ok='AGCT'
s=list(input())
cnt=0
ans=0
for si in s:
  if si in ok:
    cnt+=1
  else:
    ans = max(ans,cnt)
    cnt=0
ans = max(ans,cnt)
print(ans)