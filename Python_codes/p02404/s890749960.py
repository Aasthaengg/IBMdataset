H = []
W = []
i = 0
while True:
  h, w = map(int, input().split())
  H.append(h)
  W.append(w)
  if H[i] == 0 and W[i] == 0:
    break
  i += 1

i = 0
while True:
  if H[i] == 0 and W[i] == 0:
    break
  for k in range(W[i]):
    print("#", end = "")
  print()
  for j in range(H[i] - 2):
    print("#", end = "")
    for k in range(W[i] - 2):
      print(".", end = "")
    print("#")
  for k in range(W[i]):
    print("#", end = "")
  print()
  print()
  i += 1