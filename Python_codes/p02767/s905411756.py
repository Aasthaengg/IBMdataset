N = int(input())
X = list(map(int, input().split()))
 
ans = 10000000000
for i in range(100):
  s = 0
  for j in range(N):
    s += (X[j]-i)**2
    
  ans = min(ans, s)
  
print(ans)