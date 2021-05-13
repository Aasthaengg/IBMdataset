N, x = [int(x) for x in input().strip().split()]
an = sorted([int(a) for a in input().strip().split()])
cumsum = 0
ans = 0
for i, a in enumerate(an, start=1):
  cumsum += a
  if cumsum > x:
    break
  ans = i
else:
  if cumsum != x:
    ans -= 1
print(ans)