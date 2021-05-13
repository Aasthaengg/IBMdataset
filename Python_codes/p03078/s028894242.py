from heapq import heappush, heappop

x, y, z, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
# used = [[[False] * (z + 1) for _ in range(y + 1)] for _ in range(x + 1)]
used = set()
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
kouho = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]


def calc(a, b, c):
    if not (a, b, c) in used:
        used.add((a, b, c))
        heappush(kouho, ((-A[a] - B[b] - C[c]), a, b, c))


used.add((0, 0, 0))
for i in range(k):
    temp, p, q, r = heappop(kouho)
    print(-temp)
    if p + 1 < x:
        calc(p + 1, q, r)
    if q + 1 < y:
        calc(p, q + 1, r)
    if r + 1 < z:
        calc(p, q, r + 1)
