s=int(input())
p=[]
p.append(s)
i=1
while s!=0:
  if s%2==0:
    s=int(s/2)
  else:
    s=3*s+1
  i+=1
  if s in p:
    print(i)
    break
  p.append(s)