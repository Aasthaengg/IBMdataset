from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]

sushi.sort(key=lambda x: x[1])
kinds = defaultdict(int)
eaten = []
ans = 0
for i in range(k):
    neta, point = sushi.pop()
    kinds[neta] += 1
    ans += point
    heapq.heappush(eaten, [point, neta])

num_of_kinds = len(kinds.keys())
ans += num_of_kinds ** 2
candidate = ans

for i in range(k):
    point, neta = heapq.heappop(eaten)
    if kinds[neta] == 1:
        continue
    kinds[neta] -= 1

    while sushi:
        new_neta, new_point = sushi.pop()
        if kinds[new_neta] >= 1:
            continue
        else:
            break
    else:
        break
    kinds[new_neta] += 1
    num_of_kinds += 1
    delta = new_point - point + (2*num_of_kinds - 1)
    candidate += delta
    ans = max(ans, candidate)

print(ans)