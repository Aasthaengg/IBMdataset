N=int(input())
if N==1 :
  print(1)
  exit()
for i in range(1,N+1) :
  if i*i>N :
    print((i-1)*(i-1))
    exit()