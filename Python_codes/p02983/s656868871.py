L, R = map(int, input().split())
if L+2019 <= R:
  print(0)
else:
  m = 2019
  for a in range(L, R+1):
    for b in range(a+1, R+1):
      m = min(m, ((a%2019)*(b%2019))%2019)
  print(m)