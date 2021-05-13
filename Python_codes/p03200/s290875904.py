s=input()
ans,cnt=0,0
for i in range(len(s)):
  if s[i]=="B":
    cnt+=1
  else:
    ans+=cnt
print(ans)