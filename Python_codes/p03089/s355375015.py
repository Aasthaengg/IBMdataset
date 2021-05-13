n,*b=map(int,open(0).read().split())
b=[0]+b
ans=[]
for i in range(n):
  for i in range(len(b)-1,0,-1):
    if i==b[i]:
      ans.append(b.pop(i))
      break
  else:
    print(-1)
    exit()
for i in ans[::-1]:
  print(i)