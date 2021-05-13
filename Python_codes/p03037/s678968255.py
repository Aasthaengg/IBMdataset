N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(M)]

max_l, min_r = 0, N

for l, r in LR:
    max_l = max(l, max_l)
    min_r = min(r, min_r)
    if min_r < max_l:
        print(0)
        exit()

print(min_r - max_l + 1)
