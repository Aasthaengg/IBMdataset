from itertools import accumulate as acc
N, C = map(int, input().split())
ds, vs = [], []
for i in range(N):
  d, v = map(int, input().split())
  ds.append(d)
  vs.append(v)
rvcs = list(acc(vs))
lvcs = list(acc(vs[:: -1]))
rds = ds
lds = [C - d for d in ds[:: -1]]
re = [v - d for d, v in zip(rds, rvcs)]
le = [v - d for d, v in zip(lds, lvcs)]
remax = [0]
lemax = [0]
for i in range(N):
  remax.append(max(remax[-1], re[i]))
  lemax.append(max(lemax[-1], le[i]))
res = 0
#i個のスシを補給する時、右回り直進、左回り直進、右回り反転左回り、左回り反転右回りがある
#反転の際はエネルギー累積maxを使わないと同じスシを２回食べちゃうかも
#反転しない際は取れるだけ取らせてみてもいい
for i in range(N):
  res = max(res, re[i], le[i], re[i] + lemax[N - i - 1] - rds[i], le[i] + remax[N - i - 1] - lds[i])
print(res)