import heapq

n,m = map(int,input().split())
a = list(map(int,input().split()))
heapq.heapify(a)

B,C = [],[]
CB = []

for i in range(m):
    b,c = map(int,input().split())
    B.append(b)
    C.append(c)
    CB.append((c,b))

CB.sort(reverse=True)
for c,b in CB:
    for i in range(b):
        tmp = heapq.heappop(a)
        if tmp >= c:
            heapq.heappush(a,tmp)
            break
        else:
            heapq.heappush(a,c)
print(sum(a))