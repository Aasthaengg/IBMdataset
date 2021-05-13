W,H,N = map(int,input().split())

XW = [1] * W
YW = [1] * H

for i in range(N):
  x,y,a = map(int,input().split())
  if a == 1:
    XW[:x] = [0]*x
  elif a == 2:
    XW[x:] = [0]*(W-x)
  elif a == 3:
    YW[:y] = [0]*y
  elif a == 4:
    YW[y:] = [0]*(H-y)
print(sum(XW)*sum(YW))
    

