data = []
while True:
  m,f,r = map(int, input().split())
  if m == -1 and f == -1 and r == -1:
    break
  else:
    if m == -1 or f == -1:
      data.append("F")
    elif m + f >= 80:
      data.append("A")
    elif m + f >= 65:
      data.append("B")
    elif m + f >= 50 or r >= 50:
      data.append("C")
    elif m + f >= 30:
      data.append("D")
    else:
      data.append("F")

for i in data:
  print(i)
