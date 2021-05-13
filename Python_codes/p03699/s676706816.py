n = int(input())
sl = []
for i in range(n):
  s = int(input())
  sl.append(s)

nmul = []
for i in range(n):
  if sl[i] % 10 != 0:
    nmul.append(sl[i])

for i in range(n):
  ssl = sum(sl)
  if ssl % 10 == 0:
    if len(nmul) != 0:
      subm = ssl - min(nmul)
      print(subm)
    else:
      print(0)
    break
  else:
    print(sum(sl))
    break