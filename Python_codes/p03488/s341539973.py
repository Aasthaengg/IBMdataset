s=input()
x,y=map(int,input().split())
xpossible=[0]
ypossible=[0]
j=0
while s[j]=='F':
  j+=1
  xpossible[0]+=1
  if j==len(s):
    break
counter=0
i=j
while i<len(s):
  current=0
  while s[i]=='F':
    i+=1
    current+=1
    if i==len(s):
      break
  r=set()
  if counter==0:
    for j in xpossible:
      r.add(j+current)
      r.add(j-current)
    xpossible=[]
    for j in r:
      xpossible.append(j)
  else:
    for j in ypossible:
      r.add(j+current)
      r.add(j-current)
    ypossible=[]
    for j in r:
      ypossible.append(j)
  if i==len(s):
    break
  current=0
  while s[i]=='T':
    i+=1
    current+=1
    if i==len(s):
      break
  counter=(counter+current)%2
if x in xpossible and y in ypossible:
  print('Yes')
else:
  print('No')
