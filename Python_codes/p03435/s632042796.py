a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

if c[0]-b[0]==c[1]-b[1]==c[2]-b[2] and b[0]-a[0]==b[1]-a[1]==b[2]-a[2] and a[2]-a[1]==b[2]-b[1]==c[2]-c[1] and a[1]-a[0]==b[1]-b[0]==c[1]-c[0]:
  print('Yes')
else:
  print('No')