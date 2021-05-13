n,*l=map(int,open(0).read().split())
d={1:0,2:0,4:0}
for i in l:
  if i%2: d[1]+=1
  elif i%4: d[2]+=1
  else: d[4]+=1
if d[2]: print('YNeos'[d[1]>d[4]::2])
else: print('YNeos'[d[1]-1>d[4]::2])