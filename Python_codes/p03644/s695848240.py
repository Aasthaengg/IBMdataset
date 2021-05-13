N=int(input())
if N==1:
  print(1)
  exit()
L=[1,2,4,8,16,32,64,128]
for i in range(7):
  if L[i+1]>N:
    print(L[i])
    exit()