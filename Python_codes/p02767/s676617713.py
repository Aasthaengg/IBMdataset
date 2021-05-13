N = int(input())
X = list(map(int, input().split()))

import math

X_min = math.floor(min(X))
X_max = math.ceil(max(X))

c = [0] * (X_max - X_min + 1)

for i in range(X_min, X_max+1):
  for j in range(N):
    c[int(i)-X_min] += (X[j] - i)**2
    
d = min(c)
print(d)