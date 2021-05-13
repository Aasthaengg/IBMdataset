N,D=input().split(' ')
n,d=int(N),int(D)

XY=[input().split(' ') for i in range(n)]
xy=[[int(XY[j][i])for i in range(2)]for j in range(n)]


S=0
for i in range(n):
  x,y=xy[i]
  if x**2+y**2<=d**2:
    S+=1
print(S)