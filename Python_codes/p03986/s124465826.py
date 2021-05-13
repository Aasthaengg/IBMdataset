x = input()
scount, tcount, c = 0, 0, 0
for i in range(len(x)):
  if x[c]=="S":
    scount+=1
  else:
    if scount>0:
      scount-=1
    else:
      tcount+=1
  c+=1
print(tcount*2)