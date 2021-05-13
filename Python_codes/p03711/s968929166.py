a = [1,2,1,0,1,0,1,1,0,1,0,1]    
x,y=map(int, input().split())
if(x==2 or y == 2):
  print("No")
  exit()
if(a[x-1] == a[y-1]):
  print("Yes")
else:
  print("No")