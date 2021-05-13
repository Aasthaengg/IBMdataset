x=input()
s=t=0
for i in x:
  if i=="S":s+=1
  else:
    if s:
      s-=1
    else:
      t+=1
print(s+t)