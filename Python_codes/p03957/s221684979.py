S = input()
if "C" not in S:
  print("No")
  exit()
idx = S.index("C")
if idx == len(S) - 1:
  print("No")
  exit()
if "F" not in S[idx+1:]:
  print("No")
  exit()
print("Yes")