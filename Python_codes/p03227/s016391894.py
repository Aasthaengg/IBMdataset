S = input()
if len(S) == 2:
  print(S)
else:
  for i in range(len(S)):
    print(S[len(S) - i - 1],end = "")