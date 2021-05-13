n=list(input())
le=len(n)
if le==1:
  print(int(n[0]))
  exit()
x=list(n)
x.remove(x[0])
if len(set(x))==1 and x[0]=='9':
  key=int(n[0])
  print(9*(le-1)+key)
  exit()
m=list(n)
m.remove(m[-1])
if len(set(m))==1 and m[0]=='9':
  print(9*(le-1)+8)
else:
  key=int(n[0])
  print(9*(le-1)+key-1)