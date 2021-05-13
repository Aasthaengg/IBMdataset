a = input().split(" ")
A = int(a[0])
B = int(a[1])

if B == 1:
  print(0)
else:
  s = A
  count = 1
  while s< B:
    s += A -1
    count += 1

  print(count)