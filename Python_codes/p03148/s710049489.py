from heapq import heapify, heappush, heappop

N, K = map(int, input().split())
dts = []
for _ in range(N):
    t, d = map(int, input().split())
    dts.append((d, t-1))

dts.sort(reverse=True)

PQRem = []
isFounds = [False] * N
sumD = 0
for d, t in dts[:K]:
    sumD += d
    if isFounds[t]:
        heappush(PQRem, d)
    isFounds[t] = True
numKind = isFounds.count(True)

PQAdd = []
for d, t in dts[K:]:
    if not isFounds[t]:
        heappush(PQAdd, -d)
    isFounds[t] = True

ans = sumD + numKind**2
for x in range(numKind+1, K+1):
    if not PQRem or not PQAdd:
        break
    dRem = heappop(PQRem)
    dAdd = -heappop(PQAdd)
    sumD += -dRem + dAdd
    score = sumD + x**2
    ans = max(ans, score)

print(ans)
