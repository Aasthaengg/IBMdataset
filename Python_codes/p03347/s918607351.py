n = int(input())
a = [int(input()) for i in range(n)]
if a[0] != 0:
  print(-1)
  exit()
  
ans = 0
for i in range(1,n):
  if a[i] > a[i-1] + 1:
    ans = -1
    break
  if a[i] == a[i-1] + 1:
    ans += 1
  else:
    ans += a[i]
    
print(ans)