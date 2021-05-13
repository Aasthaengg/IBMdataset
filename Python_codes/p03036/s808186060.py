r,d,x=map(int,input().split())
listr=[]
while len(listr)<=9:
  x=r*x-d
  listr.append(x)
  
[print(i) for i in listr]