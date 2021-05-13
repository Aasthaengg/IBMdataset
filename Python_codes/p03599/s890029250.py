import bisect
A, B, C, D, E, F = map(int, input().split())
water = []
sugar = []

for i in range(F//(100*A)+1):
  for j in range(F//(100*B)+1):
    if 100*A*i + 100*B*j <= F:
      water += [100*A*i + 100*B*j]

water = list(set(water))

for i in range(F//C+1):
  for j in range(F//D+1):
    if C*i + D*j <= F:
      sugar += [C*i + D*j]

sugar = list(set(sugar))
sugar = sorted(sugar)
ans_sw = 0
ans_s = 0
ans = 0
for w in water:
  s = min((E/100)*w, F-w)
  idx = bisect.bisect_right(sugar, s)
  if w + sugar[idx-1] == 0:
    continue
  conc = (sugar[idx-1]/(w+sugar[idx-1]))*100
  if ans < conc:
    if sugar[idx-1] <= (E/100)*w and sugar[idx-1] + w <= F:
      ans = conc
      ans_sw = w + sugar[idx-1]
      ans_s = sugar[idx-1]
if ans_sw == 0:
  ans_sw = 100*A
print(ans_sw, ans_s)