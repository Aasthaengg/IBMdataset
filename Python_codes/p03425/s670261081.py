from itertools import combinations
N = int(input())
X = ["M","A","R","C","H"]
Y = [0 for _ in range(5)]
for _ in range(N):
  S = input()
  for i, x in enumerate(X):
    if x == S[0]:
      Y[i] += 1
      break
    
ans = 0
for y in combinations(Y, 3):
  ans += y[0] * y[1] * y[2]
print(ans)