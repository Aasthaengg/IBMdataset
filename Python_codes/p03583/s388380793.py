n=int(input())
for i in range(1,3501):
  for j in range(1,3501):
    if 4*i*j-n*j-n*i>0 and i*j*n/(4*i*j-n*j-n*i)%1==0:
      print(i,j,int(i*j*n/(4*i*j-n*j-n*i)))
      exit()