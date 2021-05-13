S = input()
K = len(S)

N = S.count("o")

if N + 15 - K >= 8:
  print("YES")
else:
  print("NO")