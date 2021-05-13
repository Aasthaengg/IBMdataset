N = int(input())
xu = [list(map(str,input().split())) for _ in range(N)]

ans = 0

for x,u in xu:
  if u == 'BTC':
    ans += float(x)*380000.0
  else:
    ans += float(x)

print(ans)