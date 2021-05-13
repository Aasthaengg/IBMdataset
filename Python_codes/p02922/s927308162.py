A, B = map(int, input().split())

N = 0

if B == 1:
  N = 0
elif A >= B:
  N = 1
else:
  N = 1
  X = A
  while X < B:
    N += 1
    X = (A-1)*(N-1)+A

print(N)
