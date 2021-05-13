N = int(input())

for h in range(1, 3501):
  for n in range(1, 3501):
    if 4*n*h-N*n-N*h == 0:
      continue
    w = N*h*n/(4*n*h-N*n-N*h)
    if w > 0 and w.is_integer():
      ans = [n, h, int(w)]
print(*ans)