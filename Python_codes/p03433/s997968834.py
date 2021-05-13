N=int(input())
A=int(input())
if (N%500)==0:
  print("Yes")
elif ((N%500)-A)<=0:
  print("Yes")
elif ((N%500)-A) >0:
  print("No")