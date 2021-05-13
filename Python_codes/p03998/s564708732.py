s=[ [] for i in range(3) ]
s[0]=input()
s[1]=input()
s[2]=input()
p=0
while True:
  if len(s[p])==0:
    if p==0:
      print('A')
    elif p==1:
      print('B')
    else:
      print('C')
    exit()
  tmp=s[p][0]
  s[p]=s[p][1:]
  if tmp=='a':
    p=0
  elif tmp=='b':
    p=1
  else:
    p=2
