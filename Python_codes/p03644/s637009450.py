N = int(input())
count_max = 0
count_i = 0

for i in range(1,N+1):
  count = 0
  ii = i
  for j in range(i):
    if i%2 == 0:
      i = int(i/2)
      count += 1
    else:
      break
  if count > count_max:
    count_max = count
    count_i = ii
  elif i == 1:
    count_i = 1
print(count_i)