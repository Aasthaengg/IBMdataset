s = list(input())
n = len(s)
a = (n - 1) // 2
b = (n + 3) // 2

judge = 1

for i in range(n // 2):
  if s[i] != s[-(i + 1)]:
    judge = 0
    break

if judge == 0:
  print('No')
else:
  al = s[:a]
  bl = s[b - 1:]
  for j in range(a // 2):
    if al[j] != al[-(j + 1)]:
      judge = 0
      break
  if judge == 0:
    print('No')
  else:
    for k in range((n - b) // 2):
      if bl[k] != bl[-(k + 1)]:
        judge = 0
        break
    if judge == 0:
      print('No')
    else:
      print('Yes')