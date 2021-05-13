n=int(input())
x=[]
y=[]
h=[]
for i in range(n):
  a,b,c=map(int,input().split())
  x.append(a)
  y.append(b)
  h.append(c)
  if c!=0:q=[a,b,c]
for i in range(101):
  for j in range(101):
    H=q[2]+abs(q[0]-i)+abs(q[1]-j)
    for a,b,c in zip(x,y,h):
      if c!=max(H-abs(a-i)-abs(b-j),0):break
    else:
      print(i,j,H)
      exit()