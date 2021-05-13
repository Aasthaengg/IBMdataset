n,x,y = map(int,input().split())
r = x+y-n
if r < 0:
  r = 0
print(min(x,y),r)