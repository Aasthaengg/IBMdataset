S=input()
agct='AGCT'
ans=0
for i in range(len(S)):
  cnt=0
  j=i
  while j<len(S) and S[j] in agct :
    cnt+=1
    j+=1
  ans=max(ans,cnt)
print(ans)