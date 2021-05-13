n = int(input())
A = list(map(int, input().split()))
B = {}
C = {}
for i, a in enumerate(A):
  if i % 2 == 0:
    B[a] = B.get(a, 0) + 1
  else:
    C[a] = C.get(a, 0) + 1
Bs = sorted(B.items(), key = lambda x: x[1], reverse = True)
Cs = sorted(C.items(), key = lambda x: x[1], reverse = True)
if Bs[0][0] != Cs[0][0]:
  print(n - Bs[0][1] - Cs[0][1])
elif len(Bs) == 1:
  if len(Cs) == 1:
    print(n // 2)
  else:
    print(n - Bs[0][1] - Cs[1][1])
else:
  if len(Cs) == 1:
    print(n - Bs[1][1] - Cs[0][1])
  else:
    print(min(n - Bs[0][1] - Cs[1][1], n - Bs[1][1] - Cs[0][1]))