n,c=map(int,input().split())
x,y,z=-1,-1,-1
for i in range(n+1):
  for j in range(n+1-i):
    if 10000*i+5000*j+(n-i-j)*1000==c:
      x,y,z=i,j,n-i-j
      print(x,y,z)
      exit()
print(x,y,z)