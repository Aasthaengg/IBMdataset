n = input()
if n == "".join(reversed(list(n))):
  print("Yes")
else:
  print("No")