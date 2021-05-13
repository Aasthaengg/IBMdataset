n=(int)(input())
a=[0 for i in range(10001)]
for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      temp = (x * x) + (x * y) + (x * z) + (y * y) + (y * z) + (z * z)
      if temp <= 10000:
        a[temp] += 1

for i in range(n):
  print(a[i + 1])