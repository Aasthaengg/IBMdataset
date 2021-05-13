x = int(input())
if x <= 3:
  print(1)
  exit()
res = 0
for i in range(2, 33):
  for j in range(2, 12):
    a = i ** j
    if a <= x:
      res = max(res, a)
print(res)