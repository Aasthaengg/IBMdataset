a,b,c = input().split(" ")
for i in range(10):
  ans = int(a)*int(c) - int(b)
  c = ans
  print(c)