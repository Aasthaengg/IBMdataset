r,d,x=map(int,input().split())
L=[]
for i in range(10):
  x = r*x - d
  L.append(x)
for j in range(10):
  print(L[j])