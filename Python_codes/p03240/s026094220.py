n = int(input())
x, y, h = zip(*[map(int, input().split()) for _ in range(n)])

h_range = {}
for cx in range(0, 101):
    for cy in range(0, 101):
        h_range[(cx, cy)] = [1, 10000000000]

for i in range(n):
    for (cx, cy) in h_range.keys():
        ch_max = h[i] + (abs(cx - x[i]) + abs(cy - y[i]))
        if h[i] == 0:
            ch_min = 0
        else:
            ch_min = ch_max
        ch_range = h_range[(cx, cy)]
        h_range[(cx, cy)] = [max(ch_min, ch_range[0]), min(ch_max, ch_range[1])]

for (cx, cy) in h_range.keys():
    ch_range = h_range[(cx, cy)]
    if ch_range[0] <= ch_range[1]:
        for ch in range(ch_range[0], ch_range[1] + 1):
            print('{} {} {}'.format(cx, cy, ch))
