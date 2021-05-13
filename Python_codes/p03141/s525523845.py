import heapq
N = int(input())
AB = []
for i in range(N):
    ab = list(map(int, input().split()))
    AB.append([-ab[0] - ab[1], -ab[0], -ab[1]])

AB.sort(reverse=True)

heapq.heapify(AB)
ans = 0
for i in range(N):
    q = heapq.heappop(AB)
    if i % 2 == 0:
        ans += - q[1]
    else: ans += q[2]
print(ans)