a=int(input())
b=a%10
if int(a/10)==9:
  print("Yes")
else:
  if b==9:
    print("Yes")
  else:
    print("No")