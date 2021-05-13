n=int(input())
x=[-1]*n
y=[-1]*n
h=[-1]*n
for i in range(n):
  x[i],y[i],h[i]=map(int,input().split())
  
cnt=0
now=0
for i in range(n):
  if h[i]>0:
    cnt+=1
    now=i
if cnt==1:
  print(x[now],y[now],h[now])
  exit()

for cx in range(0,101):
  for cy in range(0,101):
    H=[]
    for i in range(n):
      if h[i]>0:
        H.append(h[i]+abs(cx-x[i])+abs(cy-y[i]))
    if len(set(H))==1:
      print(cx,cy,H[0])
      exit()
