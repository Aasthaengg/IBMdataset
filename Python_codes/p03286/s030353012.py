n = int(input())
if n == 0:
  print(0)
  exit(0)
s = ""
while n != 0:
  m = abs(n % -2)
  s = str(m) + s
  n = (n - m) // -2
print(s)