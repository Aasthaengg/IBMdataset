c=[list(map(int,input().split())) for _ in range(3)]

a0=0
b0=c[0][0]-a0
b1=c[0][1]-a0
b2=c[0][2]-a0

a1= c[1][0]-b0
a2= c[2][0]-b0
if a1 == c[1][1]-b1 == c[1][2]-b2\
and a2 == c[2][1]-b1 == c[2][2]-b2:
  print("Yes")
else:
  print("No")