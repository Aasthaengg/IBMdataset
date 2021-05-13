import sys
input = sys.stdin.readline
A, B, C, D, E, F = map(int, input().split())
s = set()
for i in range(31):
  for j in range(31):
    if (i * A + j * B) * 100 <= F:
      s.add((i * A + j * B) * 100)
    else: break
s.discard(0)
#print(s)
ss = set()
for i in range(3001):
  for j in range(3001):
    if i * C + (j * D) <= F:
      ss.add(i * C + j * D)
    else: break
resw = 100 * A
ress = 0
for water in s:
  for suger in ss:
    if water // 100 * E >= suger and (water + suger <= F):
      if suger * (resw + ress) > (ress * (water + suger)):
        resw = water
        ress = suger
print(resw + ress, ress)