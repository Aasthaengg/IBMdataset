x = input().split()
a = int(x[0])
b = int(x[1])
count = 0
for i in range(0, 2):
  if a >= b:
    count += a
    a -= 1
  elif a <= b:
    count += b
    b -= 1
print(count)