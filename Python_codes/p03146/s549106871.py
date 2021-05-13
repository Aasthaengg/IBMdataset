s = int(input())
a = []

for i in range(1,1000001):
  if i == 1:
    a.append(s)
  elif s%2 == 0:
    s = s/2
    if s in a:
      print(i)
      exit()
    else:
      a.append(int(s))
  elif s%2 == 1:
    s = 3*s+1
    if s in a:
      print(i)
      exit()
    else:
      a.append(int(s))