n=input()
c=0
for i in range(len(n)):
  if n[i]=='o':
    c+=1
if c>0:
  print(700+(c*100))
else:
  print(700)
