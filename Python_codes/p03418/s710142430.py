n, k = map(int, input().split())

ans = 0

if k == 0:
  print(n**2)
  exit()

for b in range(k+1, n+1):
  c = n//b
  r = n%b
  #print((b-k)*c+max(0, r-k+1))
  ans += (b-k)*c+max(0, r-k+1)
print(ans)