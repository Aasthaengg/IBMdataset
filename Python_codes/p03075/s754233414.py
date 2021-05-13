L = []
for _ in range(6):
  L.append(int(input()))

if L[4]-L[0] <= L[5]:
  print("Yay!")
else:
  print(":(")