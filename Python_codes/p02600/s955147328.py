A = int(input())
for i in range(8):
  if A < 400 + (i+1)*200:
    print(8-i)
    break
  else:
    continue

