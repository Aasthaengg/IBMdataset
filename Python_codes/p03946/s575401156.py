n,t = map(int,input().split())
a = list(map(int,input().split()))
mdic = {}
mx = 0
import heapq
h = []
heapq.heappush(h,a[0])

for i in range(1,n):
    if mx == a[i]-h[0]:
        mdic[mx] += 1
    if mx < a[i]-h[0]:
        mx = a[i]-h[0]
        mdic[mx] = 1
    heapq.heappush(h,a[i])
#print(h[0])
mlist = sorted(list(mdic.items()))
#print(mlist)
print(mlist[-1][1])

