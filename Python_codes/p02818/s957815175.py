i = input().split()
a = int(i[0])
b = int(i[1])
k = int(i[2])
if a >= k:
  a = a - k
else:
  if (k - a) >= b:
    a = 0
    b = 0
  else:
    b = b - (k - a)
    a = 0
print(a," ",b)