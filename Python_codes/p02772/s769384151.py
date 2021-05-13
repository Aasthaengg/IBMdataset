n = int(input())
vals = list(map(int, input().split()))

qual = all(v % 2 == 1 or (v % 3 == 0 or v % 5 == 0) for v in vals)

if qual:
  print('APPROVED')
else:
  print('DENIED')
