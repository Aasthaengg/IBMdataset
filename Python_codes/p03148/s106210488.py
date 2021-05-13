from heapq import heappush,heappop,heapify

n,k = map(int,input().split())

# とりあえずネタは無視しておいしさが大きい寿司からk個を選び(hq)、満足ポイントを計算する。
# それに選ばれなかった寿司から、選ばれた寿司のネタにはないネタで、かつ、
# そのネタの中でおいしさが最大のものを選んでおく(rhq)。
# hqのうち、hqのネタ種類数が減らなように選んだおいしさが最小のものと、
# rhqのうちおいしさが最大のものを入れ替えて、満足ポイントを計算する。
# (こうすると、おいしさの合計は減るがネタの種類数は増える。)
# これを繰り返して、最大の満足ポイントを出力する。

td = []
for i in range(n):
  td.append(tuple(map(int,input().split())))
td.sort(key = lambda x:(x[0],-x[1]))

tf = [False for _ in range(n)]
s = []
for t,d in td:
  t -= 1
  if tf[t]:
    s.append((0,d)) #そのネタの中でおいしさ最大でないもの
  else:
    s.append((1,d)) #そのネタの中でおいしさ最大のもの
    tf[t] = True

s.sort(key = lambda x:-x[1])
#print(s)
hq = s[:k]
heapify(hq)

rhq = []
for t,d in s[k:]:
  if t == 1:
    rhq.append(-d)
heapify(rhq)

ans = 0
tsum = 0
dsum = 0
for t,d in hq:
  tsum += t
  dsum += d
ans = dsum+tsum**2

while(True):
  t,d = heappop(hq)
  if t == 1:
    break
  if len(rhq) == 0:
    break
  newd = heappop(rhq)
  dsum += -newd-d
  tsum += 1
  ans = max(dsum+tsum**2,ans)
print(ans)
