from math import sqrt
X = int(input())
N = int(sqrt(X))
ans = N**2
for i in range(N,0,-1):
  for j in range(X):
    if abs(X-i**j) < abs(X-ans) and i**j <= X:
      ans = i**j

print(ans)