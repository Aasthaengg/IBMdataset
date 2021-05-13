n=int(input())
d={}
for x in range(n):
  key=input()
  if key not in d:
    d[key]=0
  d[key]+=1
  
values=d.values()
a=max(values)
b=[]
for y in d:
  if d[y]==a:
    b.append(y)
    
b=sorted(b)
for r in b:
  print(r)