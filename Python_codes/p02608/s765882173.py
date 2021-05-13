ans = [0] * 10000
for x in range(1, 101):
  for y in range(1, 101):
    for z in range(1, 101):
      k = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
      if k > 10000:
        break
      ans[k - 1] += 1

n = int(input())
for i in range(n):
  print(ans[i])