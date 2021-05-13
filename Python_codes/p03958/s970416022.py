import heapq

buf = []
heapq.heapify(buf)

k,t = map(int,input().split())
arr = list(map(int,input().split()))

for a in arr:
    heapq.heappush(buf,-a)

ans = 0

bef = None
while True:
    if not bef and len(buf) == 0:
        break
    if len(buf) == 0:
        ans += abs(bef)
        break
    else:
        top = heapq.heappop(buf)
        if bef:
            heapq.heappush(buf,bef)

        if top == -1:
            bef = None
        else:
            top += 1
            bef = top




    # print(buf,bef)


print(ans)