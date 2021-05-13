N = int(input())
X = list(map(int, input().split()))
 
ans = 10**9
m = min(X)
M = max(X)
for i in range(m, M+1):
  s = 0
  for j in range(N):
    s += (X[j]-i)**2
  ans = min(ans, s)
  
print(ans)