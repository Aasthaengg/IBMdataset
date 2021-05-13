S = input()
N = len(S)
S = S[:] + "X"
T = ""
i, j = 0, 0
X = 0
def excAB(n, lis):
  y = 0
  m = len(lis)
  for i in range(m):
    y += n - 1 - i - lis[m-1-i]
  return y

M = []
while i < N:
  if S[i] == 'A':
    T = T[:] + "A"
    i += 1
    M.append(j)
    j += 1
  elif S[i:i+2] == "BC":
    T = T[:] + "B"
    i += 2
    j += 1
  else:
    X += excAB(j, M)
    T = T[:] + "C"
    M = []
    i += 1
    j = 0
X += excAB(j, M)
print(X)