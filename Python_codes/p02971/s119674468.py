n=int(input())
l=[]
for _ in range(n):
  l.append(int(input()))
m=max(l)
mc=l.count(m)
tin=set(l)
if len(tin)==1:
  s=m
else:
  s=sorted(tin)[-2]
for i in l:
  if i==m:
    if mc>1:
      print(m)
    else:
      print(s)
  else:
    print(m)
