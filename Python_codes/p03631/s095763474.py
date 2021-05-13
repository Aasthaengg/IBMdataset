s = list(input())
x = int("".join(s))
y = int("".join(s[::-1]))
if x == y:
  print("Yes")
else:
  print("No")
