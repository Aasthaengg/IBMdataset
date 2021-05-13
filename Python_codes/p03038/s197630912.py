from collections import Counter
import heapq

n,m = map(int,input().split())
l = list(map(int,input().split()))

hq  = sorted(tuple(Counter(l).items()), key=lambda x:x[0])

heapq.heapify(hq)
# print(hq)
BC = [list(map(int, input().split())) for i in range(m)]
BC = sorted(BC,key = lambda x:-x[1])

for b,c in BC:
    while b > 0:
        x,y = heapq.heappop(hq)
        if x < c:
            if b < y:
                heapq.heappush(hq,(c,b))
                heapq.heappush(hq,(x,y-b))
                b = 0
            else:
                heapq.heappush(hq,(c,y))
                b -= y
        else:
            heapq.heappush(hq,(x,y))
            break
    # print(hq)

ans = 0
for i in range(len(hq)):
    ans += hq[i][0]*hq[i][1]
print(ans)