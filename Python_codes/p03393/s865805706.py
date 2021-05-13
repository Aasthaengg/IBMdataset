S = input()
words = [chr(c) for c in range(ord("a"), ord("z")+1)]
if S == "".join(words[::-1]):
  print(-1)
elif len(S) != 26:
  for c in words:
    if c not in S:
      print(S + c)
      exit()
else:
  for i in range(1, 26):
    for j in range(i+1):
      if S[-(i+1)] < S[-(j+1)]:
        print(S[:-(i+1)] + S[-(j+1)])
        exit()