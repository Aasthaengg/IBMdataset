n,k = map(int,input().split())

ans = 0 
for b in range(1,n+1):
  x = n // b
  r = n % b
  ans += x * max(0, b - k)
  ans += max(0, r - k + 1)
  if k == 0:
    ans -= 1
    
print(ans)    