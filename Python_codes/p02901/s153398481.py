n, m = map(int, input().split())
keys = dict()
min_cost = dict()
for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    bit = 0
    for x in c:
        bit |= 1 << (x - 1)
    if bit in keys and keys[bit] <= a:
        continue
    keys[bit] = a
    min_cost[bit] = a

for i in range(1, 1 << n):
    if not i in min_cost:
        continue 
    for bit, cost in keys.items():
        bit |= i
        if i != bit:
            if bit in min_cost:
                min_cost[bit] = min(min_cost[bit], min_cost[i] + cost)
            else:
                min_cost[bit] = min_cost[i] + cost

if not (1 << n) - 1 in min_cost:
    print(-1)
else:
    print(min_cost[(1 << n) - 1])