import itertools
n,k = map(int,input().split())

ab = [0]*n

for i in range(n):
  ab[i] = input().split()
a = []
b = []
for i in range(n):
  tmp1 = int(ab[i][0])
  tmp2 = int(ab[i][1])
  a.append(tmp1)
  b.append(tmp2)
ab = zip(a,b)
ab = sorted(ab)
a,b = zip(*ab)

s = 0
for i in range(n):
  s += int(b[i])
  if s >= k:
    print(int(ab[i][0]))
    exit()