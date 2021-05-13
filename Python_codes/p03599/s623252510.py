import itertools
A, B, C, D, E, F = map(int, input().split())
U = F
water = [0]*(U+1)
water[0] = 1
for i in range(U+1):
    if water[i]:
        if i+100*A <= U:
            water[i+100*A] = 1
        if i+100*B <= U:
            water[i+100*B] = 1
water_val = [val for val in range(1, U+1) if water[val]]
suger = [0]*(U+1)
suger[0] = 1
for i in range(U+1):
    if suger[i]:
        if i+C <= U:
            suger[i+C] = 1
        if i+D <= U:
            suger[i+D] = 1

suger_val = [val for val in range(U+1) if suger[val]]
max_c = -1
for w, s in itertools.product(water_val, suger_val):
    if E*w < 100*s:
        continue
    if F < w+s:
        continue

    if max_c < 100*s/(w+s):
        max_c = 100*s/(w+s)
        ans = (w+s, s)

print(*ans)
