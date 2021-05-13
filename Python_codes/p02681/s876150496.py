S = input()
T = input()

if (T.find(S) == 0) & (len(T) - len(S) == 1):
  print("Yes")
else:
  print("No")