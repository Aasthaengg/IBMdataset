N = int(input())
 
ans = ":("
 
for X in range(N+1):
  if int(X * 1.08) == N:
    ans = X
    break
    
print(ans)
