a=0
x=y=''
for i,s in enumerate(input()[::-1]):
  y+=s
  if x!=y:
    a+=1
    x=y
    y=''
print(a)