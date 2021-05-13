w, a, b = map(int, input().split())

aw = a+w
bw = b+w

if (a <= b <= aw) or (a <= bw <= aw):
  print(0)
elif b>a:
  print(b-aw)
else:
  print(a-bw)