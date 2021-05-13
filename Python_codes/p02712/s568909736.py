N= int(input())
ls = []

for i in range(N+1):
  if i % 3 == 0 and i % 5 == 0:
    ls.append(0)
  elif i % 3 == 0:
    ls.append(0)
  elif i % 5 == 0:
    ls.append(0)
  else:
    ls.append(i)

print(sum(ls))
