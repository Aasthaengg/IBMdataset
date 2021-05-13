N = int(input())
D = {i: 1 for i in range(3, 55556, 2)}
D[2] = 1
for i in range(3, 237, 2):
  if D[i] == 1:
    for j in D:
      if j % i == 0 and j != i:
        D[j] = 0
L = []
for i in D:
  if D[i] == 1:
    L.append(i)
X = [[] for i in range(5)]
for i in L:
  X[i%5].append(i)
S = []
for i in range(N):
  S.append(X[1][i])
for i in range(N):
  if i != N - 1:
    print(S[i], end = ' ')
  else:
    print(S[i])