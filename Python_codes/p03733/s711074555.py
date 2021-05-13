N, T = map(int, input().split())
t = list(map(int, input().split()))
X = 0
for i in range(N - 1):
  if t[i+1] - t[i] > T:
    X += T
  else:
    X += t[i+1] - t[i]
print(X + T)