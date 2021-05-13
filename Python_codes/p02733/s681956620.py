from itertools import accumulate
from operator import add


h, w, k = map(int, input().split())

white_count = [0] * (w+1)
prev = [0] * (w+1)
for _ in range(h):
    line = iter('0'+input())
    cumsum_1d = accumulate(map(int, line))
    cumsum_2d = list(map(add, prev, cumsum_1d))
    prev = cumsum_2d
    white_count += cumsum_2d


def get_white(sy, sx, ny, nx):
    a = sy*(w+1) + sx
    b = sy*(w+1) + nx
    c = ny*(w+1) + sx
    d = ny*(w+1) + nx
    return white_count[d] - white_count[c] - white_count[b] + white_count[a]


ans = []
for pattern in range(2**(h-1)):
    dived = [0] + [y+1 for y in range(h-1) if (pattern>>y) & 1] + [h]
    slash_count = len(dived) - 2

    prev_x = 0
    for div_x in range(1, w + 1):
        for idx in range(len(dived)-1):
            prev_y = dived[idx]
            div_y = dived[idx+1]
            white = get_white(prev_y, prev_x, div_y, div_x)
            if white > k:
                break
        else:
            continue

        slash_count += 1
        if prev_x == div_x - 1:
            break
        prev_x = div_x - 1

    else:
        ans.append(slash_count)

print(min(ans))