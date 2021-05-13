N = int(input())

x=""
while N!=0:
  x=str(N%(2))+x
  N=-(N//2)
print(0 if x=="" else x)