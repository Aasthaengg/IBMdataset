n,m,x,y=map(int,input().split())
xt=list(map(int,input().split()))
yt=list(map(int,input().split()))
xt.sort()
yt.sort()
if max(x,xt[len(xt)-1])<min(y,yt[0]):
  print("No War")
else:
  print("War")