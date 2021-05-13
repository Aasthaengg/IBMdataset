import sys
s=list(input())

if "L" not in s[::2] and "R" not in s[1::2]:
  print("Yes")
else:
  print("No")

