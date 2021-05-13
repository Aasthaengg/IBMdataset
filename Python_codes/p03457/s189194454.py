n = int(input())
ti_1, xi_1, yi_1 = [0,0,0]
for i in range(n):
  ti, xi, yi = map(int, input().split())
  tlim = ti- ti_1
  dist = abs(xi - xi_1) + abs(yi - yi_1)
  if tlim < dist or (tlim-dist) % 2 == 1:
    print('No')
    exit()
  else:
    ti_1, xi_1, yi_1 = ti, xi, yi
    continue
print('Yes')