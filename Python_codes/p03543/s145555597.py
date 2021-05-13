from collections import Counter

N = list(input())

a = len(set(N[:-1]))
b = len(set(N[1:]))

if a == 1 or b == 1:
  print("Yes")
else:
  print("No")