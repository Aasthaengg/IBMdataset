S = input()
if S.count("C") > 0:
  k = S.index("C")
  if S[k+1:].count("F") > 0:
    print("Yes")
    exit()
print("No")