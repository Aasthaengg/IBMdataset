n = int(input())
l = list(map(int, input().split()))
sl = []

ma, mi = max(l), min(l)
if ma == mi:
  sl.append(0)

for x in range(mi, ma):
  s = 0
  for i in l:
    s += (i - x)**2 
  sl.append(s)

print(min(sl))