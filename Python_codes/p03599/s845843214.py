a, b, c, d, e, f = map(int, input().split())
water = [False for _ in range(31)]
water[0] = True
for g in [a, b]:
    for i in range(31):
        if i - g < 0:
            continue
        elif water[i - g]:
            water[i] = True
            
salt = [False for _ in range(3001)]
salt[0] = True
for g in [c, d]:
    for i in range(3001):
        if i - g < 0:
            continue
        elif salt[i - g]:
            salt[i] = True

water_cand = []
for i, tf in enumerate(water):
    if tf:
        water_cand.append(i * 100)
salt_cand = []
for i, tf in enumerate(salt):
    if tf:
        salt_cand.append(i)
        
ans = [0, 0]
max_ratio = -1
for w in water_cand:
    if w == 0:
        continue
    for s in salt_cand:
        if w + s > f:
            break
        if w // 100 * e < s:
            break
        ratio = 100 * s / (w + s)
        if max_ratio < ratio:
            max_ratio = ratio
            ans = [w + s, s]
print(*ans)