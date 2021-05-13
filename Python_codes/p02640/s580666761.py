inp = [int(a) for a in input().split()]
head = float(inp[0])
leg = float(inp[1])

kame = (leg - head * 2) / 2
turu = head - kame

if kame == int(kame) and kame * turu >= 0:
  print ("Yes")
else:
  print ("No")


