N = int(input())
H = list(map(lambda h: int(h), input().split(" ")))

maxH = []
for i in range(len(H)):
  if i == 0:
    maxH.append(H[i])
  else:
    maxH.append(max([H[i],maxH[i-1]]))

impossible = False
for i in range(len(H)):
  if maxH[i] - H[i] >= 2:
    impossible = True

print("No") if impossible else print("Yes")