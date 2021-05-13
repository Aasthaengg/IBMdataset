n = input().split()
a = int(n[0])
b = int(n[1])
c = a+b
if c >= 24:
  c -= 24
print(c)