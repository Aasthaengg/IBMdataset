S = input()
length = len(S)
for i in range(length):
  if i > 0 and len(S) % 2 == 0:
    if S[:len(S) // 2] == S[-len(S) // 2:]:
      print(len(S))
      break
  S = S[:-1]
