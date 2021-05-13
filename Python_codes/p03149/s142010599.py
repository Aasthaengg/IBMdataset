x=list(map(int,input().split()))
x.sort()
k=1000*x[0]+x[1]+10*x[2]+100*x[3]
if k==1974:
  print("YES")
else:
  print("NO")