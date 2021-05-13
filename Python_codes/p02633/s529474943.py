x=int(input())
for i in range(1,200):
  i*=360
  if(i%x==0):
    print(i//x)
    exit()