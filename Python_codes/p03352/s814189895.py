x = int(input())
box = []
for i in range(1,32):
  for j in range(2,9):
    if i**j <= x:
      box.append(i**j)
    else:
      break
print(max(box))