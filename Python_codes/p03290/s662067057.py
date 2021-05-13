d,g = map(int,input().split(" "))
li=[]
for x in range(d):
  li.append(list(map(int,input().split(" "))))

sum=[]
for i in range(2**(d)):
  s=0
  a=0
  z=[]
  for j in range(d):
    if i >> j & 1:
      s += li[j][0]*100*(j+1) + li[j][1]
      a += li[j][0]
    else:
      z.append(j)

  if s >= g:
    sum.append(a)
  else:
    k = max(z)
    h = g-s
    for l in range(li[k][0]):
      if l*(k+1)*100 >= h:
        sum.append(a+l)
        
print(min(sum))