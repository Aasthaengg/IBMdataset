s=list(input())
wd=""
bef=""
ans=0
for i in s:
  wd+=i
  if bef!=wd:
    ans+=1
    bef=wd
    wd=""
    
print(ans)