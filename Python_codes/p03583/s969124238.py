n = int(input())
for i in range(1, 3501):
  for j in range(1, 3501):
    seed = 4 * i * j - n * (i + j) 
    if seed > 0:
      k, mod = divmod(n * i * j, seed) 
      if mod == 0:
        print(i, j, k)
        exit()
