#Pythonのままだときびしい？
#100*100*200*100
n=int(input())
x=[-1]*n
y=[-1]*n
h=[-1]*n
for i in range(n):
  x[i],y[i],h[i]=map(int,input().split())

mh=max(h)
for cx in range(0,101):
  for cy in range(0,101):
    for H in range(mh,mh+216):
      if all(h[j]==max(H-abs(cx-x[j])-abs(cy-y[j]),0) for j in range(n)):
        print(cx,cy,H)
        exit()
