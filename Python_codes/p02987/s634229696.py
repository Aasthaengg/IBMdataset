S = str(input())
cnt = 0
cha = []
for s in S:
  if s not in cha:
    cha.append(s)
  elif s == cha[0]:
    cnt += 1
  
if len(cha)==2 and cnt==1:
  print('Yes')
else:
  print('No')