N, M = [int(i) for i in input().split()]
AC = 0
WA = 1

ac_count = 0
wa_count = 0
data = {}
for _ in range(M):
  p, s = input().split()
  if p in data:
    if data[p][AC] == 1:
      # AC済のものはスキップ
      continue
  if s == "AC":
    if p in data:
      wa_count += data[p][WA]
    ac_count += 1
    data[p] = [1, 0]
  if s == "WA":
    if p in data:
      data[p][WA] += 1
    else:
      data[p] = [0, 1]

print(ac_count, wa_count)
