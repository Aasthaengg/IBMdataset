x = int(input())
a = x//11
b = x%11
if b > 6:
  c = 2
elif b > 0:
  c = 1
else:
  c = 0
print(2*a+c)