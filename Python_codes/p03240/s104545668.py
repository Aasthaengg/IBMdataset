from itertools import product
xyh = []
xyh0 = []
N=int(input())
for _ in range(N):
    tmp1, tmp2, tmp3 = map(int, input().split())
    if tmp3 > 0:
        xyh.append((tmp1, tmp2, tmp3))
    else:
        xyh0.append((tmp1, tmp2, tmp3))
ans = None
for cx, cy in product(range(101), repeat=2):
    H = None
    H_lower = 1
    H_upper = 10**100
    is_ok = 1
    for x, y, h in xyh:
        if H is None:
            H = abs(x-cx)+abs(y-cy)+h
        else:
            if H != abs(x-cx)+abs(y-cy)+h:
                is_ok = 0
                break
    if not is_ok or H is None:
        continue
    for x, y, h in xyh0:
        H_upper = min(H_upper, abs(x-cx)+abs(y-cy))
    if H > H_upper or H < H_lower:
        continue
    ans = (cx, cy, H)
    break

print(*ans)