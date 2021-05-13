K = int(input())
S = str(input())

if len(S) <= K:
  print(S)
else:
  s = ''
  for i in range(K):
    s += S[i]
  s += '...'
  print(s)
