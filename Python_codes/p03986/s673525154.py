s=input()
cnt,ans=0,len(s)
for ss in s:
  if ss=="S":
    cnt+=1
  else:
    if cnt>0:
        cnt-=1
        ans-=2
print(ans)