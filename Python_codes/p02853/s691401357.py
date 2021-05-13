a = list(map(int, input().split()))
ans = 0
prise = {1: 300000, 2: 200000, 3: 100000}
for i in a:
  if i not in prise:
    continue
  ans += prise[i]
if a[0] == a[1] == 1:
  ans += 400000
print(ans)