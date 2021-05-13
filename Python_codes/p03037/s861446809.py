N,M = map(int,input().split())

bottom = 0
top = N+1

for i in range(M):
  L,R = map(int,input().split())
  bottom = max(bottom, L)
  top = min(top,R)
  
ans = top - bottom + 1
print(ans if ans>=0 else 0)