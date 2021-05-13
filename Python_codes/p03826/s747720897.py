a=list(map(int,input().split()))

b=a[0]*a[1]
c=a[2]*a[3]

if b-c>0:
  print(b)

else:
  print(c)