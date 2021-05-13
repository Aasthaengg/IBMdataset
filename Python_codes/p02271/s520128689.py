n = int(input())
A = list(map(int, input().split()))
q = int(input())
L = list(map(int, input().split()))
X = list()
for bit in range(1<<n):
  A2 = list()
  for i in range(n):
    if bit & (1<<i):
      A2.append(A[i])
  X.append(sum(A2))
for i in range(q):
  if L[i] in X:
    print('yes')
  else:
    print('no')
