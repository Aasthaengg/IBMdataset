N = int(input())
X = list(map(int, input().split()))

Y = sorted(X)
m = Y[N//2 - 1]
M = Y[N//2]

for i in X:
  if i <= m:
    print(M)
  else:
    print(m)