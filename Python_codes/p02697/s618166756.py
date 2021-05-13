n,m=map(int,input().split())
if n&1:
  for i in range(m):
    print(i+1,n-i)
else:
  a=0
  for i in range(m):
    if n&2:
      if i+1==(n//2+1)//2:a=1
    elif i+1==n//2//2+1:a=1
    print(i+1+a,n-i)