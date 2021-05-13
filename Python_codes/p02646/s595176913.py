A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

dist = abs(B-A)
r_vel = V - W

if r_vel * T >=dist:
  print("YES")
 
else:
  print("NO")