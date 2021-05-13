h = int(input())
w = int(input())
n = int(input())
count = 0
if h < w:
  a = w
  b = h
else:
  a = h
  b = w
 
x = int(n/a)
if n%a != 0:
  x += 1
print(x)