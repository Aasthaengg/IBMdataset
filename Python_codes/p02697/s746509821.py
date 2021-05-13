n, m = map(int, input().split())

if m%2 == 0:
    gu_max, ki_max = m, m-1
else:
    gu_max, ki_max = m-1, m
gu_start = 1
ki_start = 1 + gu_max + 1

for sa in range(m)[::-1]:
    sa += 1
    if sa%2 == 0:
        print(gu_start, gu_start+sa)
        gu_start += 1
    else:
        print(ki_start, ki_start+sa)
        ki_start += 1