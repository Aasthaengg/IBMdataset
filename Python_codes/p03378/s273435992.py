N, M, X = map(int, input().split())
A = list(map(int, input().split()))
b = 0
c = 0
for a in A:
  if a < X:
    b += 1
  else:
    c += 1
print(min(b, c))