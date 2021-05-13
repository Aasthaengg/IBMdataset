a, b  = map(int, input().split())
count = 0
for i in range(b):
  temp = a + i
  if temp > b:
    break
  li = []
  ni = temp
  for p in range(4):
    li.append(ni // (10 ** (4 - p)))
    ni = ni % (10 ** (4 - p))
  li.append(ni % 10)
  if li == li[::-1]:
    count += 1
print(count)