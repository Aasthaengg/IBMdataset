r,d,x = map(int, input().split())

def calc_weight(r, d, x):
  return r*x-d

for _ in range(10):
  x = calc_weight(r, d, x)
  print(x)