a=input()
b=0
c=0
for i in range(len(a)):
  if a[i]=="A" or a[i]=="C" or a[i]=="G" or a[i]=="T":
    b=b+1
    if c<b:
      c=b
  if a[i]!="A" and a[i]!="C" and a[i]!="G" and a[i]!="T":
    b=0
print(c)