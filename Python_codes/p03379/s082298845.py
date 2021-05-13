n = int(input())
X = list(map(int,input().split()))
h = int(n/2)
Xs = sorted(X)
m1 = Xs[h-1]
m2 = Xs[h]

for i in range(n):
  if X[i] <= m1:
    print(m2)
  else:
    print(m1)