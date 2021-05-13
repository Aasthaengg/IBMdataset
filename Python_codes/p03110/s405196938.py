n = int(input())

ans = 0
for i in range(n):
  x,u = input().split()
  x = float(x)
  if u=='JPY': ans += x
  if u=='BTC': ans += 380000.0*x

print(ans)
