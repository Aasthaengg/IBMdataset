X=int(input())
check=[False]*(X+1)
check[1]=True
for i in range(2,X+1):
  temp=i*i
  while temp<=X:
    check[temp]=True
    temp*=i
for i in range(X,0,-1):
    if check[i]==True:
      print(i)
      exit()
