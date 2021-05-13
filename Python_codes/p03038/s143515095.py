import heapq
n, m = map(int, input().split())
aas = sorted(list(map(int, input().split())))
hq = []
for i in range(m):
    b, c = map(int, input().split())
    heapq.heappush(hq,(-c,b))
i = 0
while hq:
    c, b = heapq.heappop(hq)
    c = -c
    for j in range(i,min(n,i+b)):
        if aas[j] < c:
            aas[j] = c
        else:
            print(sum(aas))
            exit()
    i = j + 1
print(sum(aas))