r, d, x = map(int, input().split())
xi = x
for i in range(10):
  xi *=  r 
  xi -= d
  print(xi)