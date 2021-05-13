n = int(input())
for c in range(26):
  for d in range(16):
    if 4 * c + 7 * d == n:
      print('Yes')
      exit()
print('No')