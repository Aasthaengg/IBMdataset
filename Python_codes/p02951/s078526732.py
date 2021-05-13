x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = c - (a - b)
if d < 0:
  d = 0
print(d)