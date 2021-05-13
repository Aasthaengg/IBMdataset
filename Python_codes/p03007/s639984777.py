n,a=int(input()),sorted(list(map(int,input().split())))
q,p=b,c=a[0],a[-1]
d=a[1:-1]
for i in d:
  if i<0:p-=i
  else:q-=i
print(p-q)
for i in d:
  if i<0:print(c,i);c-=i
  else:print(b,i);b-=i
print(c,b)
