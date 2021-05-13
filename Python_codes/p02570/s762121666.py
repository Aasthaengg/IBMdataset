D, T, S = map(int,input().split())
t = D / S

if t<=T or D == 0:
  print("Yes")
elif S == 0 or T == 0:
  print("No")
else:
  print("No")