n = int(input())
for i in range(1,3501):
  for j in range(1,3501):
    if 4*i*j-n*j-n*i:
      if (n*i*j)/(4*i*j-n*j-n*i) == (n*i*j)//(4*i*j-n*j-n*i) and (n*i*j)//(4*i*j-n*j-n*i) > 0:
        print(i,j,(n*i*j)//(4*i*j-n*j-n*i))
        quit()