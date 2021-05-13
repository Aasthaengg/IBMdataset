s=input()

ans='No'

for i,ss in enumerate(s):
  if i%2==0:
    if ss =='R' or ss=='U' or ss=='D':
      ans ='Yes'
    else:
      ans='No'
      break
  else:
    if ss=='L' or ss=='U' or ss=='D':
      ans='Yes'
    else:
      ans='No'
      break
print(ans)