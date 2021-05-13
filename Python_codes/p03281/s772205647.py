n = int(input())
b = 0
for i in range(1, n+1):
  if i % 2 == 1:
    a = 0
    for j in range(1, i+1):
      if i % j == 0:
        a += 1
    if a == 8:
      b += 1
print(b)