S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
invalpha = "zyxwvutsrqponmlkjihgfedcba"
D = {alpha[i]: i for i in range(26)}
E = [0 for i in range(26)]

for i in range(len(S)):
  E[D[S[i]]] = 1
if min(E) == 0:
  for m in range(26):
    if E[m] == 0:
      S = S[:] + alpha[m]
      break
  print(S)
elif S == "zyxwvutsrqponmlkjihgfedcba":
  print(-1)
else:
  p = 26
  for i in range(25, 0, -1):
    if D[S[i]] < D[S[i-1]]:
      p = i
    else:
      break
  m = D[S[p-2]]
  L = []
  for x in range(p-1, 26):
    if D[S[x]] >= m + 1:
      L.append(S[x])
  L.sort()
  if L != []:
    S = S[:p-2] + L[0]
  else:
    S = S[:p-2] + 'z'
  print(S)