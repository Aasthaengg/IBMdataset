N = int(input())
tc, xc, yc = 0, 0, 0
ans = 'Yes'
for i in range(N):
  t, x, y = map(int, input().split())
  if (t - tc - abs(x-xc) - abs(y-yc)) % 2 == 1 or t - tc - abs(x-xc) - abs(y-yc) < 0:
    ans = 'No'
    break
  tc, xc, yc = t, x, y
print(ans)