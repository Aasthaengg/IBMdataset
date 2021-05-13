n,x = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
ans = 0
for i in range(n):
  x -= line[i]
  if x < 0:
    break
  else:
    ans += 1
    
  if i == n-1 and x != 0:
    ans -= 1
print(ans)
