n, d = map(int, input().split())
num = 2*d+1
h = n//num
if h*num == n:
  print(h)
else:
  print(h+1)