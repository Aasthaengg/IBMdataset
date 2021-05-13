W,H,X,Y = map(int,input().split())
S = W*H/2

if X==W/2 and Y==H/2:
  print(S,1)
else:
  print(S,0)