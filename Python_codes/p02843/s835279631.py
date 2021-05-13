N=int(input())
b=0
for x in range(1,N//100+1):
  for y in range(100*x,105*x+1):
    if N==y:
      print(1)
      exit()
print(0)