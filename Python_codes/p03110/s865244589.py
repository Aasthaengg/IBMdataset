N = int(input())
x = []
u = []
for i in range(N):
  X, U = map(str,input().split())
  x.append(float(X))
  u.append(U)
  
rate = 380000.0
ans = 0
  
for i in range(N):
  if u[i] == 'JPY':
    ans += x[i]
  else:
    ans += x[i] * rate
    
print(ans)