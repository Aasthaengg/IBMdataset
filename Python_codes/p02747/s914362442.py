S = input()
while len(S) != 0:
  if S[:2] == "hi":
    S = S[2:]
  else:
    break
print("Yes" if len(S) == 0 else "No")