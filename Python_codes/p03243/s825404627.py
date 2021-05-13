N=int(input())
for i in range(N,999+1):
  check=str(N)
  if check[0]==check[1]==check[2]:
    print(N)
    exit()
  N+=1
