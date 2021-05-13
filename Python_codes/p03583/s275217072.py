N = int(input())

for h in range(1,3501):
  for n in range(1,3501):
    if 4*h*n-n*N-h*N <= 0:
      continue
    if N*h*n % (4*h*n-n*N-h*N) == 0:
      w = N*h*n // (4*h*n-n*N-h*N)
      print("{} {} {}".format(h,n,w))
      exit()