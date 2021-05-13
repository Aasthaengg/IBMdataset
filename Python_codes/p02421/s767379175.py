tpoint = hpoint = 0

for _ in range(int(input())):
  tcard, hcard = input().split()
  if tcard > hcard:
    tpoint += 3
  elif tcard < hcard:
    hpoint += 3
  else:
    tpoint += 1
    hpoint += 1

print(tpoint, hpoint)