import sys
n = int(sys.stdin.readline())
m = map(int, sys.stdin.read().split())
ab = list(zip(m, m))
res = 0
for i, j in ab[::-1]:
  mmod = (i + res) % j
  if mmod:
  	res += j - mmod
print(res)
