S = input()
T = input()

for i in range(len(S) - len(T),-1,-1):
  for j in range(len(T)):
    if S[j + i] != "?" and S[j + i] != T[j]:
      break
  else:
    S = S.replace("?","a")
    print(S[:i] + T + S[i + len(T):])
    break
else:
  print("UNRESTORABLE")