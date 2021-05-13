a = input().upper()
b = input().upper()
c = input().upper()
t = "A"

while True:
  if t == "A":
    if len(a)<1:
      t = "A"
      break
    t = a[0]
    a = a[1:]
  elif t == "B":  
    if len(b)<1:
      t = "B"
      break
    t = b[0]
    b = b[1:]
  elif t == "C":
    if len(c)<1:
      t = "C"
      break
    t = c[0]
    c = c[1:]


print(t)