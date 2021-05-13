a = int(input())
b = int(input())
c = int(input())
d = int(input())

sum = 0
if a >= b:
  sum += b
else:
  sum += a
if c >= d:
  sum += d
else:
  sum += c

print(sum)