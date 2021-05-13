a,b,n=list(map(int,input().split()))

if b-1 <= n:
  print(int(a*(b-1)//b))
else:
  print(int(a*n//b))