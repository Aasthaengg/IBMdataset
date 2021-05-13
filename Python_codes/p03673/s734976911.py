n = int(input())
a = input().split()
ar = list(reversed(a))
ans = []
if not n % 2:
  for i in range(0, n, 2):
    ans.append(ar[i])

  for i in range(0, n, 2):
    ans.append(a[i])

  print(' '.join(ans))
else:
  for i in range(0, n, 2):
    ans.append(ar[i])

  for i in range(1, n, 2):
    ans.append(a[i])

  print(' '.join(ans))