N=int(input())
for i in range(N//4+1):
  if (N%(4*(i+1)))%7==0:
    print("Yes")
    break
else:
  for j in range(N//7+1):
    if (N%(7*(j+1)))%4==0:
      print("Yes")
      break
  else:
    if N%4==0 or N%7==0:
      print("Yes")
    else:
      print("No")