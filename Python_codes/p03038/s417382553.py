import heapq


change = []
n, m = map(int, input().split())
a = [-1 * int(i) for i in input().split()]
for i in range(m):
    b, c = map(int, input().split())
    change.append([-c, b])

l = []
heapq.heapify(change)
heapq.heapify(a)
flg = False
cnt = 0
while cnt < n:
    if change:
        atmp = -1 * a[0]
        btmp = -1 * change[0][0]
        if atmp <= btmp:
            b, c = heapq.heappop(change)
            while c > 0 and cnt < n:
                l.append(b)
                c -= 1
                cnt += 1
        else:
            aa = heapq.heappop(a)
            l.append(aa)
            cnt += 1
    else:
        aa = heapq.heappop(a)
        l.append(aa)
        cnt += 1
        
print(-1 * sum(l))