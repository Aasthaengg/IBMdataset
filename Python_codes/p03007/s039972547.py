N = int(input())
A = list(map(int, input().split()))
ap = []; am = []
for a in A:
  if a > 0:
    ap.append(a)
  else:
    am.append(a)

if ap and am:
  print(sum(ap) - sum(am))
  ap_last = ap.pop()
  am_base = am.pop()
  while ap:
    a = ap.pop()
    print(am_base, a)
    am_base -= a
  print(ap_last, am_base)
  ap_last -= am_base
  while am:
    a = am.pop()
    print(ap_last, a)
    ap_last -= a
elif ap:
  ap.sort(reverse=True)
  ap_base = ap.pop()
  print(sum(ap) - ap_base)
  ap_last = ap.pop()
  while ap:
    a = ap.pop()
    print(ap_base, a)
    ap_base -= a
  print(ap_last, ap_base)
else:
  am.sort()
  am_base = am.pop()
  print(am_base - sum(am))
  while am:
    a = am.pop()
    print(am_base, a)
    am_base -= a