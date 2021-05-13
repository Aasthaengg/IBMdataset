A=list(input())
B=list(input())
C=list(input())
t="a"
while True:
  if t=="a":
    if not A:
      print("A")
      break
    else:
      t=A.pop(0)
  elif t=="b":
    if not B:
      print("B")
      break
    else:
      t=B.pop(0)
  else:
    if not C:
      print("C")
      break
    else:
      t=C.pop(0)
