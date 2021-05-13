n = int(input())
ans = 0
for i in range(n):
  x,n = input().split()
  x = float(x)
  if n == "BTC":
    x *= 380000.0
  ans += x
print(ans)