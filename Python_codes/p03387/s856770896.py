a = sorted(list(map(int, input().split(" "))))
count = 0
a[0] += a[2] - a[1]
count += a[2] - a[1]

if (a[2] - a[0]) % 2 == 0:
  print(count +  ((a[2] - a[0]) // 2))
else:
  print(count +  ((a[2] - a[0]) // 2) + 2)