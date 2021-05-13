S = input()
if len(S) != 26:
  A = [0] * 26
  offset = ord('a')
  for s in S:
    A[ord(s)-offset] = 1
  print(S + chr(A.index(0)+offset))
elif S == 'zyxwvutsrqponmlkjihgfedcba':
  print(-1)
else:
  k = 25
  while S[k-1] > S[k]:
    k -= 1
  X = sorted(S[k-1:])
  print(S[:k-1] + X[X.index(S[k-1]) + 1])