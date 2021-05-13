s=input()
p=input()
match=False
for i in range(len(s)):
  if s[i]==p[0]:
    if len(p)>1:
      for j in range(1,len(p)):
        if s[(i+j)%len(s)]!=p[j]:
          break
        if j==len(p)-1:
          match=True
    else:
      match=True

if match==True:
  print('Yes')
else:
  print('No')
