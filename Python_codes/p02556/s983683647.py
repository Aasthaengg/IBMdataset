n = int(input())
zm = -2e10
zn = 30000000000
wm = -2e10
wn = 30000000000
while(n):
  x,y = map(int,input().split())
  zm = max(zm,x+y)
  zn = min(zn,x+y)
  wm = max(wm,x-y)
  wn = min(wn,x-y)
  n-=1
  
print(max(zm-zn,wm-wn))
