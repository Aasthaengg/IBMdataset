S = input()
L = len(S)
A = [0 for i in range(L)]
f = 0
c = 0
P = 0
for i in range(L):
  if S[i] == "R":
    if f == 0:
      c += 1
    else:
      A[P] += c // 2
      A[P+1] += (c+1) // 2
      c = 1
      f = 0
  else:
    if f == 1:
      c += 1
    else:
      P = i-1
      A[P] += (c+1) // 2
      A[P+1] += c // 2
      c = 1
      f = 1
A[P] += c // 2
A[P+1] += (c+1) // 2
for a in A:
  print(a)