A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

AB = abs(A - B)
VW = V - W

if VW == 0:
  print("NO")
  
elif AB <= VW * T:
  print("YES")

else:
  print("NO")
