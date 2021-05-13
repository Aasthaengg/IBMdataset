n = int(input())
if n%10 == (n-n%100)/100:
  print("Yes")
else:
  print("No")