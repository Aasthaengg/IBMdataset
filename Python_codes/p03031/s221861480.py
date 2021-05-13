n, m = map(int, input().split())
bulbs = []
for _ in range(m):
    b = tuple(map(int, input().split()))
    bulbs.append(b[1:])

p = list(map(int, input().split()))

ans = 0

for switch in range(2**n):
    check = [0] * m
    for i, bulb in enumerate(bulbs):
        cnt = 0
        for b in bulb:
            if switch >> (b-1) & 1:
                cnt += 1
            
        if cnt % 2 == p[i]:
            check[i] = True
        else:
            check[i] = False
    
    if  all(check):
        ans += 1

print(ans)