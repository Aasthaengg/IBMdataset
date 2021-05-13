n,x,t=map(int,input().split())

i=int(n/x)
j=int(n%x)

if j==0:
  print(t*i)
else:
  print(t*i + t)