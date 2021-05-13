s=input()
ans,cnt=0,0
for a in s:
  if a=='B':
    cnt+=1
  else:
    ans+=cnt
print(ans)