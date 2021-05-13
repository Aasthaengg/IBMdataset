from heapq import heappush, heappop
N, K = map(int, input().split())
TD = [list(map(int, input().split())) for _ in range(N)]
TD.sort(key=lambda x:x[1], reverse=True)
muptiple = set()
for i in range(len(TD)):
    flg = 0
    if TD[i][0] not in muptiple:
        muptiple.add(TD[i][0])
        flg = 1
    TD[i][0] = flg
TD.reverse()
ret = []
point = 0
vari = 0
total = 0
for i in range(K):
    v = TD.pop()
    vari += v[0]
    point += v[1]
    if not v[0]:
        heappush(ret, v[1])

total = vari ** 2 + point

while len(TD) > 0 and len(ret) > 0:
    v = TD.pop()
    if v[0] == 0:
        continue
    pre_t = heappop(ret)
    point -= pre_t - v[1]
    vari += 1
    tmp = vari ** 2 + point
    total = max(total, tmp)

print(total)