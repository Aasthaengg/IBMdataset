S = input()
T = 'abcdefghijklmnopqrstuvwxyz'
if S == T[::-1]:
  print(-1)
  exit()
if len(S) != 26:
  for i in T:
    if i not in S:
      print(S+i)
      exit()
k = 25
while S[k-1] > S[k]:
  k -= 1
X = S[k-1]
Y = list(S[k-1:])
Y.sort()
print(S[:k-1] + Y[Y.index(X) + 1])