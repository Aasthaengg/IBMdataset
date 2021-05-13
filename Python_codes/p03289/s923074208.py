S=list(str(input()))
if S[0]!='A':
  print('WA')
  exit()
l=len(S)
flag=0
for i in range(1,l):
  if i in range(2,l-1):
    if S[i]=='C' and flag == 0:
      flag = 1
    elif S[i]=='C' and flag == 1:
      print('WA')
      exit()
    elif S[i].isupper():
      print('WA')
      exit()
  elif S[i].isupper():
    print('WA')
    exit()
if flag == 1:
  print('AC')
else:
  print('WA')
