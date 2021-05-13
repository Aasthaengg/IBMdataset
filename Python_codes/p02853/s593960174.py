x,y = map(int,input().split())
s=[0,]
d={
  1:300000,
  2:200000,
  3:100000,
}

if x in d:
  s.append(d[x])

if y in d:
  s.append(d[y])

if x==1 and y==1:
  s.append(400000)
  
print(sum(s))
