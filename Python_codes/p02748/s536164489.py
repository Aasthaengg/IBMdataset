A, B, M = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
Ds = []
for i in range(M):
  x, y, c = map(int, input().split())
  x, y = x-1, y-1
  D = As[x]+Bs[y]-c
  Ds.append(D)
r = min(min(As)+min(Bs), min(Ds))
print(r)
