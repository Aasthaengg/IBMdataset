N=int(input())
for i in range(26):
  for j in range(16):
    if 4*i+7*j==N:
      print('Yes')
      exit(0)
    if 4*i+7*j>N:
      break
print('No')