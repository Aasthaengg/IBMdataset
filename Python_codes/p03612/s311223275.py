N = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(N):
  if p[i] == i+1:
    p[i] = -1
  else:
    p[i] = 0
    
for j in range(N-1):
  if p[j] == -1:
    ans += 1
    p[j] = 0
    p[j+1] = 0
if p[N-1] == -1:
  ans += 1
print(ans)
    
