ax, av = map(int, input().split())
bx, bv = map(int, input().split())
t = int(input())
 
x = abs(ax - bx)
v = av - bv
dis = v * t
 
if dis >= x:
  print("YES")  
else:
  print("NO")
