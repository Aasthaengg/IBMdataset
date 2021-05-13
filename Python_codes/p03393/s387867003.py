S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
  print(-1)
  exit()
if len(S) != 26:
  L = [0]*26
  for i in range(len(S)):
    L[ord(S[i])-97] = 1
  for i in range(26):
    if L[i] == 0:
      print(S + chr(97+i))
      exit()
else:
  B = []
  for i in reversed(range(26)):
    if ord(S[i]) > ord(S[i-1]):
      U = i
      M = i-1
      B += [ord(S[i])]
      break
    else:
      B += [ord(S[i])]
  B.sort()
  for i in B:
    if chr(i) > S[M]:
      print(S[:M] + chr(i))
      exit()