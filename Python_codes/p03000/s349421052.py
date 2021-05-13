N, X = map(int, input().split())
L = list(map(int, input().split()))
c = 1
d = 0
for i in range(N):
  d += L[i]
  if d > X:
    break
  c += 1
print(c)