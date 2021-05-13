h,w,d=map(int,input().split())
a=[list(map(int,input().split()))for i in range(h)]
num=[[]for i in range(h*w+1)]
num[0]=([0,0])
for i in range(h):
  for j in range(w):
    num[a[i][j]].extend([i,j])
cumsum=[0]*(h*w+1)
for i in range(d,h*w+1):
  x1,y1=num[i]
  x2,y2=num[i-d]
  cumsum[i]+=cumsum[i-d]+abs(x1-x2)+abs(y1-y2)
Q=int(input())
for _ in range(Q):
  x,y=map(int,input().split())
  print(cumsum[y]-cumsum[x])