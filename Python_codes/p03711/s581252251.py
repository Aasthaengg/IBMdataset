a=list(map(int, input().split()))
s=[[1,3,5,7,8,10,12],[4,6,9,11],[2]]
ans=[]
for i in a:
  for j in range(len(s)):
    if i in s[j]:
      ans.append(j)
      break
if len(set(ans))==1:
  print('Yes')
else:
  print('No')