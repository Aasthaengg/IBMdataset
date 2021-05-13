n, k = map(int, input().split())
s = [x for x in input()]

start = s[0]
current = 1
prev = None
utility = 0
while k != 0 and current < n:
  if s[current] != start:
    if not prev:
      prev = current
    else:
      utility += 1
  elif prev:
    if current == n:
      utility += 1
    else:
      utility += 2
    k = k-1
    prev = None
  else:
    utility += 1
  current += 1

if prev:
  if current == n and k > 0:
    utility +=  1
  if start == 'L':
    prev = 'R'
  else:
    prev = 'L'
else:
  if start == 'R':
    prev = 'R'
  else:
    prev = 'L'
while current < n:
  if s[current] == prev:
    utility += 1
  prev = s[current]
  current += 1
print(utility)
