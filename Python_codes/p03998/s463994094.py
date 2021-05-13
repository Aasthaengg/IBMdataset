a = list(input())
b = list(input())
c = list(input())

t = a.pop(0)
while True:
  if t == "a":
    if a == []:
      print("A")
      exit()
    else: t = a.pop(0)
  elif t == "b":
    if b == []:
      print("B")
      exit()
    else: t = b.pop(0)
  elif t == "c":
    if c == []:
      print("C")
      exit()
    else: t = c.pop(0)