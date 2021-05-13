H, W, M = map(int, input().split())

countW = [0]*(W+1)
countH = [0]*(H+1)
bomb = []
for i in range(M):
    h, w = map(int, input().split())
    bomb.append((h, w))
    countH[h] += 1
    countW[w] += 1

maxW = max(countW)
maxH = max(countH)
ans = maxW + maxH - 1
countMaxW = countW.count(maxW)
countMaxH = countH.count(maxH)

sumz = 0
for i in range(M):
    h, w = bomb[i]
    if countH[h] == maxH and countW[w] == maxW:
        sumz += 1

if countMaxW*countMaxH > sumz:
    ans += 1
print(ans)
