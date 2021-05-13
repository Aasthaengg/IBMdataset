k = int(input()) + 1
gusu = []
kisu = []
for i in range(1, k):
  if i % 2 == 0:
    gusu.append(i)
  else:
    kisu.append(i)
count = 0
for i in gusu:
  for j in kisu:
    count += 1
print(count)