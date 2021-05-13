n = int(input())
L = []
R = [] # Rは右から見た値を入れる
for _ in range(n):
  s = input()
  btm = 0
  total = 0
  for c in s:
    if c == "(":
      total += 1
    else:
      total -= 1
    btm = min(btm, total)
  if total > 0:
    L.append((btm, total))
  else:
    R.append((btm - total, - total))
    
L.sort(key=lambda x: (-x[0], -x[1]))
R.sort(key=lambda x: (-x[0], -x[1]))

Lcrr_end = 0
for b, e in L:
  if Lcrr_end + b < 0:
    print("No")
    exit()
  Lcrr_end += e

Rcrr_end = 0
for b, e in R:
  if Rcrr_end + b < 0:
    print("No")
    exit()
  Rcrr_end += e

if Lcrr_end - Rcrr_end == 0:
  print("Yes")
else:
  print("No")