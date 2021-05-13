import heapq
x, y, z, k = map(int, input().split())
a = sorted(map(int, input().split()))[::-1]
b = sorted(map(int, input().split()))[::-1]
c = sorted(map(int, input().split()))[::-1]

print(a[0] + b[0] + c[0])
candidates = []
if x > 1: candidates.append((-(a[1] + b[0] + c[0]), 1, 0, 0))
if y > 1: candidates.append((-(a[0] + b[1] + c[0]), 0, 1, 0))
if z > 1: candidates.append((-(a[0] + b[0] + c[1]), 0, 0, 1))
heapq.heapify(candidates)
popped = {(1, 0, 0): 1,
          (0, 1, 0): 1,
          (0, 0, 1): 1}

for i in range(1, k):
    value, p, q, r = heapq.heappop(candidates)
    print(-value)
    try:
        popped[(p+1, q, r)]
    except:
        if p+1 < x: 
            heapq.heappush(candidates, (-(a[p+1] + b[q] + c[r]), p+1, q, r))
            popped[(p+1, q, r)] = 1
    try:
        popped[(p, q+1, r)]
    except:
        if q+1 < y: 
            heapq.heappush(candidates, (-(a[p] + b[q+1] + c[r]), p, q+1, r))
            popped[(p, q+1, r)] = 1
    try:
        popped[(p, q, r+1)]
    except:
        if r+1 < z: 
            heapq.heappush(candidates, (-(a[p] + b[q] + c[r+1]), p, q, r+1))
            popped[(p, q, r+1)] = 1
