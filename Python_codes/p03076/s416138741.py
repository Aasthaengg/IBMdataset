a=[]
b=[]
ori=[]
ans=0
for i in range(5):
  c=int(input())
  ori.append(c)
  if c%10!=0:
    a.append((c//10+1)*10)
  else:
    a.append(c)
  
  if c%10==0:
    b.append(100)
  else:
    b.append(c%10)
a.pop(b.index(min(b)))
print(ori[b.index(min(b))]+sum(a))