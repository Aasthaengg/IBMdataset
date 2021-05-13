l = list(map(int, input().split()))

if l[0] % 2 == 0 or l[1] % 2 == 0 or l[2] % 2 == 0:
  print(0)
else:
  ans = 1
  max_idx = l.index(max(l))
  for i in range(3):
    if i != max_idx:
      ans *= l[i]
  print(ans)