X=int(input())
p=[]
p.append(1)
for i in range(2,1000):
  for j in range(2,10):
    p.append(pow(i,j))
p.sort()
ans=0
for i in range(len(p)):
  if p[i]>X:
    break
  ans=p[i]
print(ans)