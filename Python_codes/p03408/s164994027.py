import collections
N = int(input())
lsN = []
for i in range(N):
    lsN.append(input())
M = int(input())
lsM = []
for i in range(M):
    lsM.append(input())

counterN = collections.Counter(lsN)
counterM = collections.Counter(lsM)
ans = 0
for key in counterN.keys():
    money = counterN[key]
    if key in counterM.keys():
        money -= counterM[key]
    ans = max(ans,money)
print(ans)