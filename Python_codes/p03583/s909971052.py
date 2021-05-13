N = int(input())

for h in range(1,3501):
  for n in range(1,3501):
    if 4*h*n - N*n - N*h != 0:
      w = (N*h*n)/(4*h*n - N*n - N*h)
    else:
      continue
    if w > 0 and w == int(w):
      print(h,n,int(w))
      exit()