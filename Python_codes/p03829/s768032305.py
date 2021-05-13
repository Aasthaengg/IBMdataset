N, A, B = map(int, input().split())
Xs = list(map(int, input().split()))
r = 0
c = Xs[0]
for i in range(1, N):
  r += min((Xs[i]-c)*A, B)
  c = Xs[i]
print(r)
