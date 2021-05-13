n = input()
if all(n[i] == n[len(n) - i - 1] for i in range(len(n) // 2)):
  print('Yes')
else:
  print('No')