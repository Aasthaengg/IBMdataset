from collections import Counter
N = int(input())
T = tuple(map(int, input().split()))
C = Counter(T)
d = dict()
sum = 0
for c in C.most_common():
  if c[1] == 0:
    break
  if d.get(c[1]):
    sum += d[c[1]]
  else:
    x = (c[1] * (c[1] - 1)) // 2
    d[c[1]] = x
    sum += x
for t in T:
  x = C[t]
  if x >= 2:
    if d.get(x):
      minus = d[x]
    else:
      minus = (x * (x - 1)) // 2
      d[x] = minus
    if d.get(x-1):
      plus = d[x - 1]
    else:
      plus = ((x - 1) * (x - 2)) // 2
      d[x - 1] = plus
    print(sum - minus + plus)
  else:
    print(sum)