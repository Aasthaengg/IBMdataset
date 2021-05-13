from heapq import heappush, heappop

x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ab = [ea + eb for ea in a for eb in b]
ab.sort()

hp = []
for e in c:
    heappush(hp, (-(e + ab[-1]), x * y - 1))

ans = []
for _ in range(k):
    yum, i = heappop(hp)
    yum = -yum
    ans.append(yum)
    if i != 0:
        yum += ab[i-1] - ab[i]
        yum = -yum
        heappush(hp, (yum, i - 1))

print(*ans, sep="\n")
