h,w,n=map(int,input().split())
d={}
s=set()
for _ in range(n):
  a,b=map(int,input().split())
  a-=1
  b-=1
  for dy in [-2,-1,0]:
    for dx in [-2,-1,0]:
      ny,nx=a+dy,b+dx
      if 0<=ny<h and 0<=nx<w and ny+2<h and nx+2<w:
        if (ny,nx) in s:
          d[(ny,nx)]+=1
        else:
          d[(ny,nx)]=1
          s.add((ny,nx))
cnt=[0]*10
q=0
for v in d.values():
  cnt[v]+=1
cnt[0]=(h-2)*(w-2)-len(s)
for i in cnt:
  print(i)