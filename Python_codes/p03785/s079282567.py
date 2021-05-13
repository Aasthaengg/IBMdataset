N,C,K = map(int,input().split())
T = [int(input()) for i in range(N)]
T.sort()
busCount = 0
pCount = 0
time = 0
firstTime = 0
for i in range(N):
    time = T[i]
    if firstTime == 0:
        firstTime = T[i]
        busCount += 1
    pCount += 1
    if time > firstTime + K:
        firstTime = T[i]
        busCount += 1
        pCount = 1
        continue
    if pCount == C:
        firstTime = 0
        pCount = 0
print(busCount)