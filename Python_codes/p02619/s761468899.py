def f_last(d, i, lt):
  idx = []
  if i in lt[0:d]:
    idx = [j+1 for j, x in enumerate(lt[0:d]) if x == i]
  else:
    idx.append(0)
  return idx[-1]

d = int(input())
lc = list(map(int, input().split()))
ls = []
lt = []
for _ in range(d):
  ls.append(list(map(int, input().split())))

for _ in range(d):
  lt.append(int(input()))

v = 0
for dd in range(1, d+1):
  v_d = 0
  for i in range(len(lc)):
    v_d += lc[i]*(dd-f_last(dd, i+1, lt))
  v = v + ls[dd-1][lt[dd-1]-1] - v_d
  print(v)