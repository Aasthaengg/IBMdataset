s = int(input())
set = {s}
for i in range(1000000):
  if s%2 == 0:
    s /= 2
  else:
    s = s*3+1
  if s in set:
    print(i+2)
    break
  set.add(s)