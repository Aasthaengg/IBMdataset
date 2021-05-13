N = int(input())
A = []
for i in range(N):
  A.append(int(input()))
S = sum(A)
if S % 10 != 0:
  print(S)
else:
  x = 10000
  for a in A:
    if a % 10 != 0:
      x = min(x, a)
  if x == 10000:
    print(0)
  else:
    print(S - x)