N = int(input())
A = []
p = 0
q = 0
for i in range(N):
  a = int(input())
  A.append(a)
  if a > p:
    q = p
    p = a
  elif a > q:
    q = a
for i in range(N):
  if A[i] == p:
    print(q)
  else:
    print(p)