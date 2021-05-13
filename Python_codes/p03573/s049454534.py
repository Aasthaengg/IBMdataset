args = input().split()
a = int(args[0])
b = int(args[1])
c = int(args[2])

if a == b:
  print(c)
elif a == c:
  print(b)
else:
  print(a)