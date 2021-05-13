x = input().split()
h = int(x[0])
a = int(x[1])
count = 0
while h > 0:
  count += 1
  h = h - a
print(count)