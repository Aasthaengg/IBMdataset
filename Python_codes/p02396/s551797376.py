n = []
i = 0

while True:
  n.append(int(input()))
  if n[i] == 0:
    break
  i += 1

for j in range(i):
  print("Case " + str(j+1) + ": " + str(n[j]))