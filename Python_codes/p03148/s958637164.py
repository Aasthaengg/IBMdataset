from heapq import heappush, heappop
N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda x:x[1], reverse=True)
muptiple = set()
hp = []
for t, d in TD:
    flg = 0
    if t not in muptiple:
        muptiple.add(t)
        flg = 1
    heappush(hp, (d*-1, flg))

ret = []
point = 0
vari = 0
total = 0
for i in range(K):
    v = heappop(hp)
    t = v[0]*-1
    vari += v[1]
    point += t
    if not v[1]:
        heappush(ret, t)

total = vari ** 2 + point

while len(hp) > 0 and len(ret) > 0:
    v = heappop(hp)
    if v[1] == 0:
        continue
    pre_t = heappop(ret)
    t = v[0]*-1
    point -= pre_t - t
    vari += 1
    tmp = vari ** 2 + point
    total = max(total, tmp)

print(total)