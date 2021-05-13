r,d,s=map(int,input().split())
l=[0]*11
l[0]=s
for i in range(10):
  l[i+1]=l[i]*r-d
  print(l[i+1])