s=input()
t=input()
letters=[]
count=[]
for i in range(len(s)):
  if s[i] in letters:
    count[letters.index(s[i])].append(i)
  else:
    count.append([i])
    letters.append(s[i])
failflag=0
for i in count:
  r=t[i[0]]
  for j in i:
    if t[j]!=r:
      failflag=1
letters=[]
count=[]
for i in range(len(s)):
  if t[i] in letters:
    count[letters.index(t[i])].append(i)
  else:
    count.append([i])
    letters.append(t[i])
for i in count:
  r=s[i[0]]
  for j in i:
    if s[j]!=r:
      failflag=1
if failflag==0:
  print('Yes')
else:
  print('No')