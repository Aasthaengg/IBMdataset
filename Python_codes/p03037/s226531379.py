n, m = map(int, input().split())
l, r = zip(*[map(int, input().split()) for _ in range(m)])

min_r = min(r)
max_l = max(l)

if min_r >= max_l:
    print(min_r - max_l + 1)
else:
    print(0)
