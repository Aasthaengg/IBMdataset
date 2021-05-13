A, B, C, D = map(int, input().split())

tt, at = 0, 0
while(A>0 and C>0):
  tt += 1
  C -= B
  if(C <= 0):
    break
  at += 1
  A -= D
if(tt > at):
  print("Yes")
else:
  print("No")