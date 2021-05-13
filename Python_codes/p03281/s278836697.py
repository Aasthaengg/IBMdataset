N = int(input())
num = 0
for i in range(1, N+1):
  if i % 2 == 0:
    pass
  else:
    a = 0
    for j in range(1, i+1):
      if i % j == 0:
        a += 1
    if a == 8:
      num += 1
print(num)