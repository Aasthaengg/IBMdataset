w,a,b=map(int,input().split())
if min(a,b) + w >= max(a,b):
  print(0)
else:
  ans = max(a,b) - min(a,b) - w
  print(ans)
