from heapq import heappop, heappush

n, nTake = map(int, input().split())
a = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[1], x[0]))

totalTaste = 0
same = []
types = set()
for i in range(nTake):
    type, taste = a[i]
    totalTaste += taste
    if type not in types:
        types.add(type)
    else:
        heappush(same, taste)

rem = []
typesRem = set()
for i in range(nTake, n):
    type, taste = a[i]
    if type not in types and type not in typesRem:
        typesRem.add(type)
        heappush(rem, -taste)

ret = totalTaste + len(types) ** 2
curTotal = totalTaste
add = 1
while same and rem:
    worst = heappop(same)
    best = heappop(rem)
    curTotal = curTotal - worst - best
    ret = max(ret, curTotal + (len(types) + add) ** 2)
    add += 1
print(ret)