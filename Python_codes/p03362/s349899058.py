N = int(input())
List = [2]
Newlist = []

for i in range(3,10**4):
  for j in List:
    if i%j == 0:
      break
  else:
    List.append(i)

for j in List:
  if j%5 == 1:
    Newlist.append(j)

for j in range(N):
  print(Newlist[j], end=" ")