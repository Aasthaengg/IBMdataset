h,w,d=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
q=int(input())
lr=[list(map(int,input().split())) for _ in range(q)]
dmap={}
for hi in range(h):
  for wi in range(w):
    dmap[a[hi][wi]-1]=(hi+1,wi+1)
dans={}
for di in range(d):
  s=di
  x,y=dmap[di]
  tmp=0
  while s<h*w:
    nx,ny=dmap[s]
    tmp+=abs(x-nx)+abs(y-ny)
    dans[(di,s)]=tmp
    x,y=nx,ny
    s+=d
for l,r in lr:
  l-=1;r-=1
  s=l%d
  print(dans[(s,r)]-dans[(s,l)])
#print(dans)