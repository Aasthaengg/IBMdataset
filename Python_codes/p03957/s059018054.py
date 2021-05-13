S = input()
A = 0
for i in range(len(S)):
  if S[i] == "F":
    A = i
if S.count("C") > 0:
  if S.index("C") < A:
  	print("Yes")
  else:
    print("No")
else:
  print("No")