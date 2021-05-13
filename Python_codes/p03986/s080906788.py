x=input()
l=[]
for i in x:
  if len(l)>0 and l[-1]=='S' and i=='T':
    l.pop()
    continue
  l.append(i)
print(len(l))