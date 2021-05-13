from operator import itemgetter

n = int(input())
XL = []
for _ in range(n):
    x, l = map(int, input().split())
    XL.append([x-l, x+l])
XL.sort(key=itemgetter(1))
INF = 10**18
cur = -INF
ans = 0
for i in range(n):
    if cur <= XL[i][0]:
        ans += 1
        cur = XL[i][1]
print(ans)
