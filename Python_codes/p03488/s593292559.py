s = input()
x, y = map(int, input().split())
n = len(s)
S = [[], []]
d = 0
f = 0
for i in range(n):
  if s[i] == 'T':
    if f != 0:
      S[d].append(f)
    d += 1
    d %= 2
    f = 0
  elif s[i] == 'F':
    f += 1
if s[n-1] == 'F':
  S[d].append(f)
if S[0] == []:
  S[0].append(0)
if S[1] == []:
  S[1].append(0)
px, py = 0, 0
if s[0] == 'F':
  px += S[0][0]
  S[0] = S[0][1:]
for i in range(len(S[0])):
  px -= S[0][i]
  S[0][i] *= 2
for i in range(len(S[1])):
  py -= S[1][i]
  S[1][i] *= 2
mpx, mpy = x - px, y - py
X = S[0][:]
Y = S[1][:]
Dx = {0: 1}
Dy = {0: 1}
for i in X:
  L = [i for i in Dx]
  for j in L:
    if i + j <= mpx and i + j not in Dx:
      Dx[i+j] = 1
for i in Y:
  L = [i for i in Dy]
  for j in L:
    if i + j <= mpy and i + j not in Dy:
      Dy[i+j] = 1

if mpx in Dx and mpy in Dy:
  print("Yes")
else:
  print("No")