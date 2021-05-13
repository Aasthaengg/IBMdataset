W,a,b=map(int,input().split())

left=a
right=a+W
if right<=b:
  print(b-right)
elif b+W<=left:
  print(left-b-W)
else:
  print(0)