N = list(input())
n = [int(num) for num in N]
s = sum(n)

if s % 9 == 0:
  print("Yes")
else:
  print("No")