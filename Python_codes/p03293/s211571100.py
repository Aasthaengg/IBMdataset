s = str(input())
t = str(input())
isOK = False
for i in range(1,len(s)+1):
  if s==t[-i:]+t[:-i]:
    isOK = True
    break
if isOK:
  print('Yes')
else:
  print('No')