n = int(input())
l = []

def func():
    pass

for i in range(n):
  if (i+1) % 3 == 0 and (i+1) % 5 == 0:
    pass
  elif (i+1) % 3 == 0:
    pass
  elif (i+1) % 5 == 0:
    pass
  else:
    l.append(i+1)
print(sum(l))