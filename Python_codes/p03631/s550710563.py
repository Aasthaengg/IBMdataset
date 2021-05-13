N=int(input())

a=N//100

b=N-a

if (N-a)%10==0:
  print("Yes")
else:
  print("No")