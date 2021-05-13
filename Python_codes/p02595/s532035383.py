import math

N, D = map(int, input().split())
X_Y = []
for i in range(N):
    X_Y.append(list(map(int, input().split())))
    
ans = 0
for n in range(N):
  x, y = X_Y[n]
  if(math.sqrt(x**2 + y**2) <= D): ans += 1

print(ans)