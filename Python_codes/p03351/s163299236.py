a, b, c, d = map(int, input().split())

ab_distance = max(a, b) - min(a, b)
bc_distance = max(b, c) - min(b, c)
ac_distance = max(a, c) - min(a, c)

if ab_distance <= d and bc_distance <= d:
  print('Yes')
elif ac_distance <= d:
  print('Yes')
else:
  print('No')
