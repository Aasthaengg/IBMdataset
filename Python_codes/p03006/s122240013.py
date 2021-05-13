n=int(input())
xys=[list(map(int,input().split())) for _ in range(n)]
vec = []
pqs = []
for i in range(n):
    for j in range(i+1,n):
        pqs.append([(xys[i][0]-xys[j][0]),(xys[i][1]-xys[j][1])])
        pqs.append([-(xys[i][0]-xys[j][0]),-(xys[i][1]-xys[j][1])])
pqs.sort()
import collections

cnt = 1
cntMax = 0
for i in range(1,len(pqs)+1):
    if i == len(pqs):
        cntMax = max(cntMax,cnt)
    elif pqs[i] == pqs[i-1]:
        cnt += 1
    else:
        cntMax = max(cntMax,cnt)
        cnt = 1
print(n-cntMax)