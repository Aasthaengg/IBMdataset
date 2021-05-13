n=int(input())
d=[]
for i in range(1,11111+1):
  m=5*i-1
  if m%2==0:
    continue
  f=3
  while f*f<m+1:
    if m%f==0 or len(d)==n:
      break
    f+=2
  else:
    d.append(m)
print(*d)