A,B,C,D = map(int,input().split())
w1 = A+B
w2 = C+D

if w1<w2:
  print("Right")
elif w1==w2:
  print("Balanced")
else:
  print("Left")