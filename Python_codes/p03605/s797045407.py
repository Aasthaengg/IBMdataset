n = int(input())

ichi = n%10
juu = int(n/10)

if ichi == 9 or juu == 9:
  print("Yes")
else:
  print("No")