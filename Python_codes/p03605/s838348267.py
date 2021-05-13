n = int(input())
# n = 100*a + 10*b +c
b = n%10
a = int(n/10)
if a ==9or b == 9:
  print("Yes")
else:
  print("No")