S1=str(input())
S2=str(input())
ans=0
for i in range(len(S1)):
  if S1[i]!=S2[i]:
    ans=1
if ans==1:
  print('No')
else:
  print('Yes')