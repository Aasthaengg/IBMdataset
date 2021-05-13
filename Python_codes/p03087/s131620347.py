N, Q = map(int, input().split())
S = input()
A = []
for i in range(N - 1):
  if S[i] == "A" and S[i+1] == "C":
    A.append(i+1)
lA = len(A)
for i in range(Q):
  l, r = map(int, input().split())
  L1 = -1
  R1 = lA
  while L1 + 1 < R1:
    C1 = (L1 + R1) // 2
    if A[C1] < l:
      L1 = C1
    else:
      R1 = C1
  L2 = -1
  R2 = lA
  while L2 + 1 < R2:
    C2 = (L2 + R2) // 2
    if A[C2] < r:
      L2 = C2
    else:
      R2 = C2
  print(L2 - L1)