a = int(input())
b = list(map(int, input().split()))
count = 0
while(1):
  flag = 0
  for i in range(0, a, 1):
    if (b[i] % 2 == 1) :
      flag = 1
  if (flag == 1) :
    break
  for i in range(0, a, 1):
    b[i] /= 2
  count += 1
print(count)