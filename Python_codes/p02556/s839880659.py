N=int(input())
xx=[]
yy=[]
for i in range(N):
  x,y=map(int,input().split())
  xx.append(x+y)
  yy.append(x-y)
xx.sort()
yy.sort()
print(max(xx[-1]-xx[0],yy[-1]-yy[0]))
