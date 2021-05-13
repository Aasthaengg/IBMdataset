N = int(input())
h = list(map(int, input().split()))
X = [10**9+7]*N
X[0] = 0
for i in range(N):
  if i-1 >= 0 and i-2 >= 0:
    X[i] = min([X[i-1] + abs(h[i]-h[i-1]),X[i-2]+abs(h[i]-h[i-2])])
  elif i-1 >= 0:
    X[i] = X[i-1] + abs(h[i]-h[i-1])
print(X[N-1])