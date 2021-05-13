s=input()
t=input()

n=len(s)

slis=[]

for i in range(n):
  if s[i] not in slis:
    slis.append(s[i])

tlis=[]

for i in range(n):
  if t[i] not in tlis:
    tlis.append(t[i])

snum=[]

for i in range(n):
  for j in range(len(slis)):
    if s[i]==slis[j]:
      snum.append(j)
      break

tnum=[]
for i in range(n):
  for j in range(len(tlis)):
    if t[i]==tlis[j]:
      tnum.append(j)


c=0
for i in range(n):
  if snum[i]!=tnum[i]:
    c+=1

if c==0:
  print("Yes")
else:
  print("No")
