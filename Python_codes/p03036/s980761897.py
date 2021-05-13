a = list(map(int, input().split()))
d = 1
c = a[2]
while d <= 10:
  c = a[0]*c-a[1]
  print(c)
  d += 1
