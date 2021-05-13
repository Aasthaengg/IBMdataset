h,w,d=map(int,input().split())
a=[list(map(int,input().split())) for i in range(h)]
dic={}
for i in range(h):
  for j in range(w):
    dic[a[i][j]]=(i,j)
cnt=[0]*(h*w+1)
for j in range(1,d+1):
  for i in range(j,h*w-d+1,d):
    y1,x1=dic[i+d]
    y2,x2=dic[i]
    cnt[i+d]=cnt[i]+abs(x2-x1)+abs(y2-y1)
q=int(input())
for _ in range(q):
  l,r=map(int,input().split())
  print(cnt[r]-cnt[l])