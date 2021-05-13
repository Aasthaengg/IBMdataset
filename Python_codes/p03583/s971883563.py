n = int(input())

for i in range(1,3501):
  for j in range(1,3501):
    a = 4*i*j-n*j-n*i 
    if a>0 and (n*i*j)%a==0:
      print(i,j,(n*i*j)//a)
      exit()