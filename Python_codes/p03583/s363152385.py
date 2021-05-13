N = int(input())

for h in range(1, 3500+1):
  for n in range(1, 3500+1):
    if 4*h*n - N*n - N*h == 0:
      continue
    w = (N*h*n) // (4*h*n - N*n - N*h)
    if w < 1 or w > 3500:
      continue
    if 4*h*n*w == N*(n*w + h*w + n*h):
      print(h, n, w)
      exit()
