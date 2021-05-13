N = int(input())

ans = 0
for n in range(N):
  x, t = input().split()
  if t == "BTC":
    ans += float(x)*380000.0
  else:
    ans += float(x)
print(ans)
