input = raw_input().split(" ")
a = int(input[0])
b = int(input[1])
c = int(input[2])

if a > b:
  temp = b
  b = a
  a = temp

if b > c:
  temp = c
  c = b
  b = temp

if a > b:
  temp = b
  b = a
  a = temp

print a, b, c