n = int(input())
alst = list(map(int, input().split()))
bef = []
aft = []
for i, a in enumerate(alst):
  if i % 2 == 0:
    bef.append(a)
  else:
    aft.append(a)
if n % 2 == 0:
  ans = aft[::-1] + bef
else:
  ans = bef[::-1] + aft
print(*ans)