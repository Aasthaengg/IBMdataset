r,d,x = map(int,input().split())
def weight(r,d,x):
  x_next = r*x-d
  return x_next
for y in range(10):
  x = weight(r,d,x)
  print(x)