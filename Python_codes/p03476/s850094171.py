ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

q = ii()
rmax = 0
qer = []
for i in range(q):
    l,r = mi()
    qer.append([l,r])
    if rmax < r:
        rmax = r

# rmaxまで計算
# 奇数かつ4n-1ではない
# 4n+1

# 素数表
import math
primeList = [2,3,5,7,11,13]
for i in range(17,rmax+1,2):
    for j in primeList:
        if j > math.sqrt(i):
            primeList.append(i)
            break
        if i % j == 0:
            break

# print(primeList)
        
def checksim(x,pl):
    if x in pl and (x+1)//2 in pl:
        return 1
    return 0

tans = [0] * (rmax+1)
tans[3] = 1
for i in range(5,rmax+1,4):
    if checksim(i, primeList):
        tans[i] = 1

# cumsum
ans = [0]*(rmax+1)
tcumsum = 0
for i in range(rmax+1):
    if tans[i] == 1:
        tcumsum += 1
    ans[i] = tcumsum

for i in qer:
    print(ans[i[1]] - ans[i[0]-1])