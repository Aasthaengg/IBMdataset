r, D, x = map(int, input().split())

ans = x
for i in range(10):
  ans = r*ans-D
  print(int(ans))