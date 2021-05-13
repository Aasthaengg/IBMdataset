odd='RUD'
even='LUD'
s=input()
flag=0
for i in range(len(s)):
  a=i+1
  if a%2==0:
    if s[i] not in even:
      flag=1
      break
  else:
    if s[i] not in odd:
      flag=1
      break
if flag==1:
  print ('No')
else:
  print ('Yes')