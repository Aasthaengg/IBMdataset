N, A, B = map(int,input().split())
ans = 0
for i in range(N+1):
  x = str(i)
  y = 0
  for j in x:
    y += int(j)
  if A <= y <= B:
    ans += i
    
print(ans)