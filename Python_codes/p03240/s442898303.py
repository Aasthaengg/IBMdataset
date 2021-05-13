N=int(input())
x=[]
y=[]
h=[]
for i in range(N):
  a,b,c=map(int,input().split())
  x.append(a)
  y.append(b)
  h.append(c)
field=[[-1 for i in range(101)] for i in range(101)]
for i in range(N):
  for j in range(101):
    for k in range(101):
      if(h[i]!=0):
        if(field[j][k]==-1):
          field[j][k]=h[i]+abs(j-x[i])+abs(k-y[i])
        elif(field[j][k]!=h[i]+abs(j-x[i])+abs(k-y[i])):
          field[j][k]=-2
      else:
        if(field[j][k]>h[i]+abs(j-x[i])+abs(k-y[i])):
          field[j][k]=-2
cx=0
cy=0
H=0
for i in range(101):
  for j in range(101):
    if(field[i][j]>=0):
      cx=i
      cy=j
      H=field[i][j]
print(cx,cy,H)