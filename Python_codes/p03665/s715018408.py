N,P = map(int, input().split())
A = list(map(int, input().split()))
x = y = 0
for i in range (N):
  if A[i]%2 == 0:
    x += 1
  else:
    y += 1
if P%2 == 0:
  print(2**N if y == 0 else 2**(N-1))
else:
  print(0 if y == 0 else 2**(N-1))