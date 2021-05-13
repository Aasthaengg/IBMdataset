INF = 10**10
n,t = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
cost = 0
l = 0
r = 1
while r<n:    
  dif = A[r] - A[l]
  if dif == cost:
    ans += 1
  elif dif > cost :
    cost = dif
    ans = 1 
  else:
    pass
  if dif <= 0:
    l = r
  r += 1
  
print(ans)  