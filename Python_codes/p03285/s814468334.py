x = int(input())

combination = []
for i in range(26):
  for j in range(15):
    total = i*4 + j*7
    combination.append(total)
print('Yes' if x in combination else 'No')