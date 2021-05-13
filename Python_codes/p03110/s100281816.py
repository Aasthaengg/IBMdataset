N = int(input())
X, U = [], []
T = 0
for _ in range(N):
  x, u = input().split()
  X.append(x)
  U.append(u)
for x, u in zip(X, U):
  if u == "JPY":
    T += int(x)
  else:
    T += float(x)*380000.0
print(T)