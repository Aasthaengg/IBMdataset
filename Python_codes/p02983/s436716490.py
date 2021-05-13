l,r = map(int,input().split())
minimum = 2019
for i in range(l,r+1):
  if minimum == 0:
    break
  for j in range(i+1,r+1):
    if (i*j)%2019 == 0:
      minimum = 0
      break
    else:
      if (i*j)%2019 < minimum:
        minimum = (i*j)%2019
print(minimum)
