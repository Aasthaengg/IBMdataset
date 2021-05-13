a = int(input())
b = [int(input()) for i in range(a)]
c = sorted(b)[-2]
d = max(b)
if b.count(d) >= 2:
  for i in range(a):
    print(d)
else:
  for i in b:
    if i == d:
      print(c)
    else:
      print(d)