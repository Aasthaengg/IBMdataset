N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for i, a in enumerate(A):
  x -= a
  if x == 0:
    print(i+1)
    exit()
  elif x < 0:
    print(i)
    exit()
print(N-1)