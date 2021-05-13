N = int(input())
for h in range(1,3501):
  for n in range(1,3501):
    a = 4 * h * n - N * (h + n)
    if a > 0:
      w,b = divmod(N * h * n, a)
      if b == 0:
        print(h,n,w)
        exit()