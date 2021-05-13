S = list(input())
S_uni = list(set(S))
if len(S_uni) == 2:
  print("Yes")
else:
  print("No")