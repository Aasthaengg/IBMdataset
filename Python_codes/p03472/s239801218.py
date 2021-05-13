import heapq
import math

n, h = map(int, input().split())
katana = [list(map(int, input().split())) for _ in range(n)]

max_a = -1
max_b = -1 # aが最大の刀のb
max_i = -1
for i in range(n):
    a, b = katana[i]
    if a > max_a:
        max_a = a
        max_i = i
    elif a == max_a and b < max_b:
        max_i = i
        max_b = b

nagetsuke = []
for i in range(n):
    a, b = katana[i]
    if b >= max_a:
        heapq.heappush(nagetsuke, -b)

ans = 0
damage = 0
while damage < h and len(nagetsuke) > 0:
    q = heapq.heappop(nagetsuke)
    damage -= q
    ans += 1

if len(nagetsuke) == 0:
    a, b = katana[max_i]
    if damage < h:
        ans += math.ceil((h-damage)/a)

print(ans)