K, X = map(int, input().split())

mn = X - K + 1
if mn < - 1000000:
  mn = -1000000
mx = X + K -1
if mx > 1000000:
  mx = 1000000
for i in range(mn, mx+1):
  print(i)