N, K = map(int, input().split())
dts = []
for _ in range(N):
    t, d = map(int, input().split())
    dts.append((d, t-1))

dts.sort(reverse=True)

tops = []
rests = []
isFounds = [False] * N
for d, t in dts:
    if isFounds[t]:
        rests.append(d)
    else:
        tops.append(d)
        isFounds[t] = True

tops.sort(reverse=True)
rests.sort(reverse=True)

xFr = max(1, K-len(rests))
xTo = min(K, len(tops))
iTop = xFr
iRest = K-xFr
sumD = sum(tops[:iTop]) + sum(rests[:iRest])
ans = sumD + xFr**2
for x in range(xFr+1, xTo+1):
    iRest -= 1
    sumD += tops[iTop] - rests[iRest]
    score = sumD + x**2
    ans = max(ans, score)
    iTop += 1

print(ans)
