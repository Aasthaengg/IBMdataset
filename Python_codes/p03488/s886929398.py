S = input()
X, Y = map(int, input().split())

SIZE = 10 ** 4

M = [0] if S[0] == "T" else []
for i in range(1, len(S)):
  if S[i] != S[i-1]:
    M.append(i)
M.append(len(S))
M = [0] + M
#print("M:", M)

L = []
for i in range(1, len(M)):
  L.append(M[i] - M[i - 1])
#print("L:", L)

for i in range(3, len(L), 2):
  L[i] += L[i - 2]
L = [0] + L
#print("L:", L)

x = 1 << SIZE
y = 1 << SIZE
#print("x:", bin(x)[2::])
#print("y:", bin(y)[2::])

for i in range(1, len(L), 2):
  dist = L[i]
  dirc = L[i - 1]
  #print("dist, dirc:", dist, dirc)
  if i == 1:
    x = x << dist
  else:
    if dirc % 2 == 0:
      x = (x << dist) | (x >> dist)
    else:
      y = (y << dist) | (y >> dist)
      
if (x >> SIZE + X) & 1 == 1 and (y >> SIZE + Y) & 1 == 1:
  print("Yes")
else:
  print("No")