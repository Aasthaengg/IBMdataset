h,w,d=map(int,input().split())
ans=[0 for _ in range(h*w+1)]
za=[[] for _ in range(h*w+1)]
for i in range(h):
  a=list(map(int,input().split()))
  for x in range(w):
    za[a[x]].append(i)
    za[a[x]].append(x)
  

for x in range(1,h*w+1):
  if x+d<=w*h:
    ans[x+d]=ans[x]+abs(za[x+d][0]-za[x][0])+abs(za[x+d][1]-za[x][1])
    
q=int(input())
for _ in range(q):
  e,f=map(int,input().split())
  print(ans[f]-ans[e])
  


