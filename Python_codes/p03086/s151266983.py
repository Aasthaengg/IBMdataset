S=input()
ans,tmp=0,0
for s in S:
  if s in ['A','T','G','C']:
    tmp+=1
  else:
    ans=max(tmp,ans)
    tmp=0
print(max(ans,tmp))