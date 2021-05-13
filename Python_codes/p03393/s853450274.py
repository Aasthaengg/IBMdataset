S = input()

if len(S) < 26:
  N = [chr(i) for i in range(97,123) if chr(i) not in S]
  print(S + N[0])
else:
  for i in range(26):
    for j in range(i+1):
      if S[-(i + 1)] < S[-(j + 1)]:
          print(S[:-(i+1)]+S[-(j+1)])
          exit()
  else:
    print(-1)
