n = int(input())
ans = 1
maxnum_devide = 0
for num in range(2, n+1):
  target = num
  num_devide = 0
  while target % 2 == 0:
    target /= 2
    num_devide += 1
  if num_devide > maxnum_devide:
    ans = num
    maxnum_devide = num_devide
print(ans)
