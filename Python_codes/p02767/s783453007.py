N = int(input())
X = list(map(int,input().split()))

X.sort()
dist = float("inf")
for i in range(X[0],X[-1]+1):
  d = 0
  for j in range(N):
    d += (i - X[j]) ** 2
  dist = min(dist,d)
  
print(dist)