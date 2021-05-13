n = int(input())
a = list(map(int, input().split()))
q = int(input())

asum = sum(a)
adic = {}

for i in a:
  if i in adic:
    adic[i] += 1
  else:
    adic[i] = 1


for i in range(q):
  b, c = map(int, input().split())
  if b in adic:
    if c not in adic:
      adic[c] = 0
    cnt = adic.pop(b)
    adic[c] += cnt
    asum += (c-b) * cnt
  print(asum)