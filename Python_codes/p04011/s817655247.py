a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0

for i in range(1,a+1):
  if i >= b+1:
    e += d
  else:
    e += c
print(e)