S = input()
a = len(set(S[1:]))
b = len(set(S[:-1]))
if a == 1 or b == 1:
  print("Yes")
else:
  print("No")