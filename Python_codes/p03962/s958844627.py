p = sorted(list(map(int, input().split())))

if p[0] == p[1]:
  if p[1] == p[2]:
    print(1)
  else:
    print(2)
elif p[1] == p[2]:
  print(2)
else:
  print(3)

