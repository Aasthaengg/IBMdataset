import math
n, h = map(int, input().split())
AB = [[0,0] for _ in range(n)]
mxA, mxB = 0, 0
for i in range(n):
    AB[i] = list(map(int,input().split()))
    if (mxB==0) or (mxA == AB[i][0] and mxB > AB[i][1]) or (mxA < AB[i][0]):
        mxA, mxB = AB[i][0], AB[i][1]

ans = 0
AB.sort(key=lambda x: x[1], reverse=True)
mxAi = AB.index([mxA,mxB])
for i in range(n):
    if i!=mxAi and AB[i][1]>mxA and h>0:
        h -= AB[i][1]
        ans += 1
if h>0:
    ans += max(1, 1+math.ceil((h-mxB)/mxA))
print(ans)