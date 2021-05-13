a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

l = []
l.append(b-a)
l.append(c-a)
l.append(d-a)
l.append(e-a)
l.append(c-b)
l.append(d-b)
l.append(e-b)
l.append(d-c)
l.append(e-c)
l.append(e-d)

if max(l) <= k:
  print("Yay!")
else:
  print(":(")