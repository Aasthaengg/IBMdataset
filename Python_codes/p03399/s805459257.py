a = int(input())
b = int(input())
c = int(input())
d = int(input())
train = 0
bus = 0
if a < b:
  train = a
else:
  train = b
if c < d:
  bus = c
else:
  bus = d
print(train+bus)