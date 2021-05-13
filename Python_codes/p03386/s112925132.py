a,b,k=map(int,input().split())
if 2*k >= b-a+1:
  print(*list(range(a,b+1)),sep='\n')
else:
  print(*list(range(a,a+k)),sep='\n')
  print(*list(range(b-k+1,b+1)),sep='\n')